# Load mysql library
import mysql.connector as con 
# Import lib for showing db table data on table formate
from beautifultable import BeautifulTable

# lets create connection with mysql
# for connecting Python with MySql need to have 3 details of mysql server
    # host: localhost
    # user: root
    # password: 
    # After createing connect need to craete database first then connect with specific databasae as passing 4th parameter
    # database: database name
db = con.connect(
    host="localhost",
    user="root",
    password="",
    database="pytest"
)
# print('\nChekc connection: ', db)

# get cursor object to run crud:
create = db.cursor(buffered=True)

# Let crete the first databasae using create refence
query = "CREATE DATABASE IF NOT EXISTS pytest"
dbcreate = create.execute(query)
# print('\ndbcreate: ', dbcreate)

# Check all existing databases
query = "SHOW DATABASES"
aldbs = create.execute(query)
# print('\nCheck all dbs: ', create)

# Fetch all db names usign loop
# for dbname in create:
#     print('DB NAME: ', dbname)

# create table: 
# for creating a table we need a column names and theire datatypes and limit of chars for each column.

# MySql datatypes:
    # number: int, float, doble
    # string: char, 
    # aplpha/num/special: varchar
    # datetime: datetime

# Manage montly expence via table: 
    # id:
    # date
    # things
    # price
    # name

query = """CREATE TABLE IF NOT EXISTS monthly_expence_1(
    id int(8) not null AUTO_INCREMENT PRIMARY KEY, 
    things varchar(500), 
    price int(6), 
    name varchar(50), 
    date timestamp)"""
create.execute(query)

# Check all existing tables:
# create.execute("SHOW TABLES")
# print('\nCheck all Tables:')
# for table in create:
#     print('\nTable Name: ', table)

# Message
def option():
    print("""
    Choose Options:
    1. Insert New Expence
    2. Read All Expence
    3. Update Any Expence
    4. Delete Any Expence
    5. Exit
    """)
    user_input = input('\nEnter your option: ')
    if user_input == '1':
        insert_expence()
    elif user_input == '2':
        read_expencs()
    elif user_input == '3':
        update_expencs()
    elif user_input == '4':
        delete_expencs()
    elif user_input == '5':
        print('\nExit')

# Let insert daily expence
def insert_expence():
    things = input('\nEntery Thing name: ')
    price = input('\nEntery price name: ')
    name = input('\nEntery your name: ')
    # values = (things, int(price), name)
    # Here we seprates values by their type like %s use for stirng values and %d use of interger or number values
    query = """INSERT INTO monthly_expence(things, price, name) VALUES('{}',{},'{}')""".format(things, price, name)
    # print(query)
    # here pass tow variabels second varibale use for passing user inpur datas
    create.execute(query)
    # # Use commit() method for inserting or updateing data
    db.commit()
    option()

# dailey_expence()

# Check all expence details
def read_expencs():
    print('\nAll Expence Details:')
    create.execute("SELECT * FROM monthly_expence ORDER BY id DESC")
    # For fetching all data form db table use fetchall() method
    all_data = create.fetchall()

    # Create beauttable obj
    bt = BeautifulTable()
    # Check lenght of rows
    bt.column_headers = ['No','ID','Thing','Price','Name','Date']
    i=1
    for row in all_data:
        print(row)
        add_no = list(row)
        add_no.insert(0, i)
        bt.append_row(add_no)
        i+=1

    print(bt)
    # option()

def update_expencs():
    print('\n Choose which entry you want to update?')
    # Call read expence fucntion to show all existing records
    read_expencs()
    # Get user input for expence id
    get_id = input('\nEnter expence ID. ')
    updated_price = input('\nEnter new price. ')
    query = f"UPDATE monthly_expence SET price={updated_price} WHERE id={get_id}"
    create.execute(query)
    db.commit()
    print('This',create.rowcount,'record is updated.')
    read_expencs()
    option()

def delete_expencs():
    print('\n Choose which entry you want to delete?')
    # Call read expence fucntion to show all existing records
    read_expencs()
    # Get user input for expence id
    get_id = input('\nEnter expence no. ')
    query = f"DELETE FROM monthly_expence WHERE id={get_id}"
    create.execute(query)
    db.commit()
    print('This',create.rowcount,'record is deleted.')
    read_expencs()
    option()

option()
# a = [1,2,3,4]
# a.insert(4, 5)
# print(a)

# Home-work
# 1. Show table data in right formate.
# 2. Via W3 School use to run update and delate as:
    # Create 2 other methods
        # udpate data
            # change any data of any row
        # delete data
            # show user all entery and provide facitly to choose any one of it and delete


# Study:
# Learn about mysql keys: like as primary key, uniqe key, super key etc...