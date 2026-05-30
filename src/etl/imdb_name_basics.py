import pandas as pd
from config.settings import sql_engine
from pipelines.utils.load import load_sql




def extract ():
    """
    Extract raw IMDb directors data from the bronze layer.
     
    Returns:
        pd.DataFrame: Raw IMDb names basics (director's data).
    """
    return pd.read_sql('SELECT * FROM bronze.imdb_name_basics',sql_engine)





def transform(df):

    """
    Transform IMDb names data by filtering directors and cleaning columns.

    This function perfomrs:
    1. Filters rows where `primaryProfession` contains "director".
    2. Selects only the relevant columns.
    3. Replaces missing death years ('\\N') with 0 and converts the column to integer.
    4. Renames columns to match the target schema.

    Returns:
        pd.DataFrame : Cleaned dataset ready for loading
    """ 
    df = (
        df.loc[df['primaryProfession'].str.contains('director'),['nconst','primaryName','birthYear','deathYear']]
        .assign(deathYear = lambda x: x['deathYear'].replace('\\N',0).astype('int'))
        .rename(columns={'nconst':'director_id','primaryName':'director_name','birthYear':'birth_year','deathYear':'death_year'})
    )
    return df





def load(df):
    """
    Load cleaned dataset into the silver layer database table.

    Args:
        df (pd.DataFrame): Cleaned director data dataset
    """ 
    load_sql(
        dataframe=df,
        table = 'imdb_name_basics',
        schema='silver',
        connection=sql_engine,
        if_exists='replace',
        index=False       
    )
