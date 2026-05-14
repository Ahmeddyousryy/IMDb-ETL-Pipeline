import pandas as pd


def load_sql(dataframe,table,schema,connection,**kwargs):
    """
     Generic DataFrame loader into a SQL database for ETL pipeline.

    Parameters:
        dataframe : dataframe to be loaded into database.
        table: target table name in the database.
        schema: Target schema name in the database
        connection: SQLAlchemy database connection engine
        **kwargs : additional arguments passed to pandas.to_csv (index=False,if_exists='replace')
    Returns:
        None
    
    """
    dataframe.to_sql(table,con = connection,schema =schema ,**kwargs)