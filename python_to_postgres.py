import psycopg2
import psycopg2.extras
import pandas as pd


def save_to_db(new_data):
    conn= psycopg2.connect('postgres://ckgoxpjf:QCM5ShnNLkFWCSfxwmipoq9YtKdh4o4g@raja.db.elephantsql.com/ckgoxpjf')

    cur=conn.cursor()
    conn.cursor()
    
    #cur.execute('CREATE TABLE hstory (id SERIAL PRIMARY KEY, date VARCHAR, message VARCHAR(50), price DECIMAL, AvgPrice DECIMAL, PurchasePrice DECIMAL);')

    insert_script= 'INSERT INTO hstory (date, message, price, AvgPrice, PurchasePrice) VALUES (%s,%s,%s,%s,%s)'
    insert_value=(new_data)
    cur.execute(insert_script,insert_value)
    conn.commit()
    cur.close()
    conn.close()



def get_data():
    conn= psycopg2.connect('postgres://ckgoxpjf:QCM5ShnNLkFWCSfxwmipoq9YtKdh4o4g@raja.db.elephantsql.com/ckgoxpjf')
    cur=conn.cursor()
    cur.execute("SELECT * FROM hstory;")
    data=(cur.fetchall())
    full_frame = pd.DataFrame(data)
    data_frame= full_frame.tail(500)
    removed_frame_columns=data_frame[data_frame.columns[1:6]]
    data_frame_changed_column_names=removed_frame_columns.rename(columns={1: 'Date/Time', 2: 'Message',3:'Price',4:'Avg Price',5:'Purchase Price'})
    cur.close()
    
    return data_frame_changed_column_names
    

    