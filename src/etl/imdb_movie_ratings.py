import pandas as pd
from config.settings import sql_engine
from pipelines.utils.load import load_sql



def extract():
    """
    Extract raw IMDb movie ratings data.
     
    Returns:
        pd.DataFrame: raw IMDb movie ratings data.
    """
    return pd.read_sql('SELECT * FROM bronze.imdb_movie_ratings',sql_engine)





def transform(df):

    """
    Transform IMDb movie ratings to match the target schema.

    This function perfomrs:
     - Renames columns to match the target schema.

    Returns:
        pd.DataFrame : dataset ready for loading
    """     
    df = df.rename(columns={'tconst':'movie_id','averageRating':'average_rating','numVotes':'votes'})

    return df





def load(df):
    """
    Load cleaned dataset into the silver layer database table.

    Args:
        df (pd.DataFrame): Cleaned movie rating dataset
    """ 
    load_sql(
        dataframe=df,
        table = 'imdb_movie_ratings',
        schema='silver',
        connection=sql_engine,
        if_exists='replace',
        index=False       
    )