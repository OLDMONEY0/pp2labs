import psycopg2
from config import config

def add_phonebook(column): 
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params) 

        cur = conn.cursor()

        cur.execute('CALL delete_one_phonebook(%s)', (column,))

        
        conn.commit()       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)
    finally: 
        if conn is not None: 
            conn.close()

add_phonebook("ALiar")
        