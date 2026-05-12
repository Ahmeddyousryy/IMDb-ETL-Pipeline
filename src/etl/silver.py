import pandas as pd
from config.settings import sql_engine
import etl.utils.transform as transform
from etl.utils.load import load_sql


def run_silver_layer():
    
    df_tmdb_movies = (
         pd.read_sql('SELECT * FROM bronze.tmdb_movies',sql_engine)
         
        # Data cleaning
         .pipe(transform.drop_duplicates,'imdb_id')
         .pipe(transform.drop_null,'imdb_id')

        # Data transformation
         .pipe(transform.convert_dates,'release_date')

        # Upper bound handling
         .pipe(transform.drop_invalid_values,'release_date',pd.Timestamp.today(),'higher')
         .pipe(transform.drop_invalid_values,'budget',600000000,'higher')
         .pipe(transform.drop_invalid_values,'revenue',3000000000,'higher')

        # Lower bound handling
         .pipe(transform.handle_invalid_values,'budget',1000,'lower')
         .pipe(transform.handle_invalid_values,'revenue',1000,'lower')
         .pipe(transform.handle_invalid_values,'runtime',10,'lower')
    )
    load_sql(dataframe=df_tmdb_movies,table='tmdb_movies',schema= 'silver',connection=sql_engine,if_exists='replace',index=False)

  



    


    
    
