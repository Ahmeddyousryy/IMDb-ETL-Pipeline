import pandas as pd

def drop_duplicates(df,subset=None):
    return df.drop_duplicates(subset=subset,keep='first')  ## remove the duplicates but keep only the first occurance


def drop_null(df , subset=None):
    return df.dropna(subset = subset)  ## drop rows with NULL


def convert_dates(df,col):
    df[col] = pd.to_datetime(df[col])  ## fix type of 'col' column to be datetime datatype
    return df


def drop_invalid_values(df, col, threshold, operator):
    if operator == 'higher':
        return df.drop(df[df[col] > threshold].index)
    elif operator == 'lower':
        return df.drop(df[df[col] < threshold].index)
    else:
        return df
        

def handle_invalid_values(df, col, threshold, operator):
    if operator == 'higher':
        df.loc[(df[col] > threshold) , col] = pd.NA
    elif operator == 'lower':
        df.loc[(df[col] < threshold) , col] = pd.NA
    else:
        pass
    return df

    

