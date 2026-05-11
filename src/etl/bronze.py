import pandas as pd
from etl.extract import extract_csv
from etl.load import load_sql
from config.settings import DATA_SOURCES
from config.settings import BRONZE_LAYER_TABLES
from config.settings import DATA_SETS
from config.settings import sql_engine



def run_bronze_layer():

    for dataset in DATA_SETS:

        df = extract_csv(DATA_SOURCES[dataset])

        load_sql(dataframe = df,
                table = BRONZE_LAYER_TABLES[dataset],
                schema='bronze',
                connection = sql_engine,
                if_exists = 'replace',
                index=False)

   