import pandas as pd
from config.settings import sql_engine
from pipelines.utils.load import load_sql

def extract():
    """
    Extract raw TMDB movies data from the bronze layer

    Returns:
        pd.DataFrame: raw movies dataset loaded from the database
    """
    return pd.read_sql('SELECT * FROM bronze.tmdb_movies',sql_engine)






def transform(df):
    """
    Clean TMDB movies dataset for silver layer.

    Steps:
    - Remove duplicates
    - Drop invalid IDs
    - Convert release_date to datetime
    - Filter future dates
    - Remove outliers in budget and revenue

    Args:
        pd.DataFrame : dataframe that will be cleaned and transformed
    
    Returns:
        pd.DataFrame : Cleaned dataset ready for loading
    """

    df = (
        df

        # Ensure unique records
        .drop_duplicates(keep="first")

        # Remove records without valid identifier
        .dropna(subset=["imdb_id"])

        # Convert release date to datetime format
        .assign(release_date=lambda x: pd.to_datetime(x["release_date"]))

        # Keep only valid historical releases
        .loc[lambda x: x["release_date"] <= pd.Timestamp.today()]

        # Remove unrealistic budget values
        .loc[lambda x: x["budget"] < 600000000]
        .loc[lambda x: x["budget"] > 100]

        # Remove unrealistic revenue values
        .loc[lambda x: x["revenue"] < 3000000000]
        .loc[lambda x: x["revenue"] > 100]
    )
    return df






def load(df):
    """
    Load cleaned dataset into the silver layer database table.

    Args:
        df (pd.DataFrame): Cleaned movies dataset
    """    
    load_sql(dataframe=df,table='tmdb_movies',schema= 'silver',connection=sql_engine,if_exists='replace',index=False)