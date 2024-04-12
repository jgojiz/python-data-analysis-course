import pandas as pd

def extract_table(con, table_name) -> pd.DataFrame:
    data = pd.read_sql(sql=f'SELECT * FROM {table_name}', con=con)
    return data

