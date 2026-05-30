import pandas as pd
from config.settings import sql_engine
from pipelines.utils.load import load_sql



def extract():
    return pd.read_sql('SELECT * FROM bronze.imdb_movie_crew',sql_engine)




def transform(df):

    movies = pd.read_sql('SELECT * FROM silver.tmdb_movies',sql_engine)

    df = (
    
        df[['tconst','directors']]
        .merge(movies,left_on='tconst',right_on='imdb_id',how='inner')[['tconst','directors']]
        .loc[lambda x: x['directors'] != '\\N']
        .loc[lambda x: x['directors'].str.len() != 19]
        .drop_duplicates()
        .rename(columns={'tconst':'movie_id','directors':'director_id'})
    )
    return df



def load(df):
    
    load_sql(
        dataframe=df,
        table = 'imdb_movie_crew',
        schema='silver',
        connection=sql_engine,
        if_exists='replace',
        index=False       
    )