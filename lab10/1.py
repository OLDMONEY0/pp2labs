import psycopg2
import csv
# Connect to your postgres DB
conn = psycopg2.connect("dbname=pp user=postgres password = 1234")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
#cur.execute("SELECT * FROM people")

column = ""

def insert(name, phone):
    insert = "INSERT INTO public.phonebook(name, phone) VALUES ('{0}', '{1}');"
    cur.execute(insert.format(name, phone)) 
    conn.commit()
def select(column):
    if column == "": 
        cur.execute("SELECT * FROM phonebook;")
        record = cur.fetchall()
        print("Result", record)
    else: 
        select = "SELECT name, phone FROM public.phonebook WHERE name = '{0}' OR phone = '{0}';" 
        cur.execute(select.format(column))
        record = cur.fetchone()
        print("Result", record)
def update(name, phone): 
    update = "UPDATE public.phonebook SET name='{0}', phone='{1}' WHERE name = '{0}';"
    cur.execute(update.format(name, phone))
    conn.commit()
def delete(name): 
    delete = "DELETE FROM public.phonebook WHERE name = '{}';"
    cur.execute(delete.format(name))
    conn.commit()
while True:
    print("choose a method: \n1)file \n2)console \n3)stop")
    method = input()

    if method == "stop": 
        break

    if method == "file": 
        file = open('phonebook.csv')
        csvreader = csv.reader(file)
        for row in csvreader: 
            name, phone = row
            insert(name, phone)
        print("file inserting completed")

    else:
        print("choose a command: \n1)insert \n2)select \n3)update \n4)delete")
        str = input() 
        if str == "insert":
            name, phone = input().split() 
            insert(name, phone)
            print("insert completed")    
        if str == "select": 
            print("write down name or phone of the table")
            column = input()
            select(column)
        if str == "update": 
            name, phone = input().split()
            update(name, phone)
            print("update completed")
        if str == "delete":
            name = input() 
            delete(name)
            print('delete completed')
