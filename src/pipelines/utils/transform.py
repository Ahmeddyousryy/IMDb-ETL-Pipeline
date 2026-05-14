import pandas as pd

def drop_duplicates(df,subset=None):
    """
    Remove duplicate rows based on specific columns

    Args:
        df : dataframe to be processed
        subset : subset of columns used to detect duplicates


    Returns:
        Dataframe without duplicates.
    """
    return df.drop_duplicates(subset=subset,keep='first')  ## remove the duplicates but keep only the first occurance



def drop_null(df , subset=None):
    """
    Remove rows with null value based on specific columns

    Args:
        df : dataframe to be processed
        subset : subset of columns used to detect nulls


    Returns:
        Dataframe without rows contain null.
    """    
    return df.dropna(subset = subset)  ## drop rows with NULL


def convert_dates(df,col):
    """
    Convert column type into datetime

    Args:
        df : dataframe to be processed
        col : column that will be converted into datetime


    Returns:
        Dataframe after converting the column type.
    """ 
    df[col] = pd.to_datetime(df[col])  ## fix type of 'col' column to be datetime datatype
    return df


def drop_invalid_values(df, col, threshold, operator):
    """
    drop rows with invalid values

    Args:
        df : dataframe to be processed
        col : column used to check validy of the value
        threshold : the threshold used to be compared to the value
        operator : this indicates whether drop rows with values 'higher' or 'lower' the threshold 


    Returns:
        Dataframe after removing rows with invalid values.
    """ 
    if operator == 'higher':
        return df.drop(df[df[col] > threshold].index)
    elif operator == 'lower':
        return df.drop(df[df[col] < threshold].index)
    else:
        return df
        

def handle_invalid_values(df, col, threshold, operator):
    """
    Replace values in a dataframe column with NA based on a threshold condition.

    Args:
        df : dataframe to be processed
        col : column used to check validy of the value
        threshold : the threshold used to be compared to the value
        operator : this indicates whether drop rows with values 'higher' or 'lower' the threshold 


    Returns:
        Dataframe after handling rows with invalid values.
    """ 
    if operator == 'higher':
        df.loc[(df[col] > threshold) , col] = pd.NA
    elif operator == 'lower':
        df.loc[(df[col] < threshold) , col] = pd.NA
    else:
        pass
    return df

