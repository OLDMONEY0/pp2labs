import psycopg2
import csv
from config import config

def add_phonebooks(names, phones): 
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params) 

        cur = conn.cursor()

        cur.execute('CALL add_new_phonebooks(%s,%s)', (names, phones))

        
        conn.commit()       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)
    finally: 
        if conn is not None: 
            conn.close()
names = []
phones = []
file = open('phonebook.csv')
csvreader = csv.reader(file)
for name, phone in csvreader: 
    names.append(name)
    phones.append(phone)
add_phonebooks(names, phones)
        