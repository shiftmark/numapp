import psycopg2 as pg
import pandas as pd
import os

from typing import Union

def get_time(item_id) -> Union[int, float]:
    # Retrieves the sleep duration value from the database.

    connection = None
    
    # Save the database table in a dataframe and set the index to "item_id".
    try:  
        connection = pg.connect(
            host='db',
            database=os.environ['DB'],
            user='postgres',
            password=os.environ['DB_PASS']
            )
        numapp_df = pd.read_sql_query('SELECT * FROM numapp', connection, index_col='item_id')
   
    except Exception as error:
        raise f"Get sleep time error - db connection failed: {error}"
    
    finally:
        if connection is not None:
            connection.close()

    return numapp_df.at[item_id, 'duration']
    