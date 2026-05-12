import pandas as pd
import os


def extract_csv(file_path,**kwargs):
    """
    Generic CSV file extractor for ETL pipeline.

    Parameters:
        file_path: path to the csv file
        **kwargs : additional arguments passed to pandas.read_csv (sep=',',header='column')
    Returns:
        the extracted csv file as a dataframe
    
    """
    df = pd.read_csv(file_path,**kwargs)
    return df


