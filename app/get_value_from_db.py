import psycopg2 as pg
import pandas as pd

def get_time(item_id):
    df = None
    try:
        conn = pg.connect(
            host='db',
            database='numapp_data',
            user='postgres',
            password='numapp'
            )
        df = pd.read_sql_query('select * from numapp', conn)    
    except:
        pass
    
    finally:
        pass

    

    return df.columns


    