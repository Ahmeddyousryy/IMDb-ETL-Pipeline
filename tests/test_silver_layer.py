import etl.utils.transform as transform
import pandas as pd




def test_transform():

    df_before = pd.DataFrame({
    "id": [1, 2, 2, 3, 4, 4, 4, 5],
    "name": ["Alice", "Bob", "Bob", "Charlie", "David", "David", "David", "Eve"],
    "age": [25, 30, 30, 35, 40, 40, 40, 28]})
    
    df_after = transform.drop_duplicates(df_before)
    assert df_after.duplicated().sum() == 0



