import pandas as pd
from etl.bronze import run_bronze_layer
from etl.silver import run_silver_layer
from config.settings import sql_engine

import etl.transform as transform


# run_bronze_layer()

run_silver_layer()





