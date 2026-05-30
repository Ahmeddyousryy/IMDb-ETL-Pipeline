import pandas as pd
from config.settings import sql_engine
from pipelines.utils.load import load_sql




def extract():
    """
    Extract raw IMDb movie titles data from the bronze layer.

    Returns:
        pd.DataFrame: Raw IMDb titles dataset.
    """    
    return pd.read_sql('SELECT * FROM bronze.imdb_movie_titles', sql_engine)






def transform(df): 
    """
    Transform IMDb dataset into a star-schema-ready structure.

    This function performs:
    1. Genre dimension creation
    2. Movie-genre bridge table creation (many-to-many mapping)
    3. Cleaning and standardization of movie title data

    Returns:
        tuple:
            - df (cleaned movie titles table)
            - genres_df (dimension table for genres)
            - bridge_df (fact bridge table for multi_values dimension)
    """

    # =========================
    #   CREATE GENRE DIMENSION TABLE
    # =========================

    genres_series = (
        df['genres']
        .str.split(',')                # split multi_genre strings into list
        .explode()                     # convert list into rows
        .str.strip()                   # remove unwanted spaces
        .replace('\\N', pd.NA)         # handle invalid values
        .dropna()                      # drop nulls
        .unique()                      # keep only unique genres
    )

    # Create dataframe of the unique genres
    genres_df = pd.DataFrame(genres_series, columns=['genre'])

    # Create surrogate key for the dataframe
    genres_df['genre_id'] = range(1, len(genres_df) + 1)

    # Reorder the columns (id,genre)
    genres_df = genres_df[['genre_id', 'genre']]




    # =========================
    #   CREATE BRIDGE TABLE (MANY-TO-MANY)
    # =========================

    bridge_df = (
        df.copy()

        # split multi-genres string into list of genres in each row
        .assign(genres=lambda x: x['genres'].str.split(','))

        # convert list into rows
        .explode('genres')

        # clean values
        .assign(genres=lambda x: x['genres'].str.strip())
        .assign(genres=lambda x: x['genres'].replace('\\N', pd.NA))

        # keep only required columns
        [['tconst', 'genres']]

        # merge with genres_df from above to map gerne into the surrogate keys created
        .merge(genres_df, left_on='genres', right_on='genre')

        .rename(columns={'tconst':'movie_id'})
        # final bridge schema
        [['movie_id', 'genre_id']]
    )


    # =========================
    #   CLEAN MOVIE TITLES TABLE
    # =========================

    # clean runtimeMinutes colum (handle missing, invalid values)
    df['runtimeMinutes'] = (
        df['runtimeMinutes']
        .replace("\\N", pd.NA)
        .replace(0, pd.NA)
        .astype('Int64')
    )
    # Convert binary flags into readable categorical values
    df['isAdult'] = df['isAdult'].map({0: 'NO', 1: 'YES'})

    # Filter invalid future years
    df = df[df['startYear'] < 2026]

    
    # FINAL SCHEMA TRANSFORMATION
    df = (
        df
        .drop(columns=['genres'])
        .rename(columns={'tconst': 'movie_id',
                         'primaryTitle': 'movie_name',
                         'isAdult': 'is_adult',
                         'runtimeMinutes': 'runtime',
                         'startYear': 'release_year'})
    )

    return df, genres_df, bridge_df





def load(df, genres_df, bridge_df):
    """
    Load transformed IMDb data into silver layer tables.

    Tables to be loaded:
    - imdb_movie_titles 
    - imdb_genres
    - imdb_movie_genre (bridge table)

    """
    load_sql(
            dataframe=genres_df,
            table='imdb_genres',
            schema='silver',
            connection=sql_engine,
            if_exists='replace',
            index=False
    )

    load_sql(
            dataframe=bridge_df,
            table='imdb_movie_genre',
            schema='silver',
            connection=sql_engine,
            if_exists='replace',
            index=False
    )

    load_sql(
            dataframe=df,
            table='imdb_movie_titles',
            schema='silver',
            connection=sql_engine,
            if_exists='replace',
            index=False
    )
