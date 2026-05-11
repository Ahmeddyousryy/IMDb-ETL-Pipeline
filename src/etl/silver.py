import pandas as pd
from config.settings import sql_engine
import etl.transform as transform


def run_silver_layer():
    
    df = pd.read_sql('SELECT * FROM bronze.tmdb_movies',sql_engine)
    df = transform.drop_duplicates(df,'imdb_id')
    df = transform.drop_null(df , 'imdb_id')
    df = transform.convert_dates(df,'release_date')
    df = transform.drop_invalid_values(df,'release_date',pd.Timestamp.today(),'higher')
    df = transform.drop_invalid_values(df,'budget',600000000,'higher')
    df = transform.drop_invalid_values(df,'revenue',3000000000,'higher')
    df = transform.handle_invalid_values(df,'budget',1000,'lower')
    df = transform.handle_invalid_values(df,'revenue',1000,'lower')
    df = transform.handle_invalid_values(df,'runtime',10,'lower')
    
    df.to_sql(name = 'tmdb_movies',con=sql_engine,schema='silver',if_exists='replace',index=False)
    
