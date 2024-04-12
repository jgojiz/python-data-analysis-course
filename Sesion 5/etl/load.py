import pandas as pd

def load_to_dw_retail(con, table_name, data):
    try:
        data.to_sql(table_name, con, if_exists = 'append', index = False)
    except Exception as e:
        print(e)