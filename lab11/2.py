import psycopg2
from config import config

def add_phonebook(name, phone): 
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params) 

        cur = conn.cursor()

        cur.execute('CALL add_new_phonebook(%s,%s)', (name, phone))

        
        conn.commit()       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)
    finally: 
        if conn is not None: 
            conn.close()

add_phonebook("almasbekovich", "+64651255486")
        