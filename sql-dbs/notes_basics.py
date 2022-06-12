#DB-API CODE SCHEME
####################################################################################################
from dbmodule import connect

connection = connect ('databasename', 'username', 'pswd')  #connection object
cursor = connection.cursor()  #cursor object

cursor.execute('select * from tablename')  #run queries
results = cursor.fetchall()

cursor.close()
connection.close()  #free resources

#METHODS
####################################################################################################

#Connection
.cursor()     #returns a new cursor object using the connections
.commit()     #commit any pending transaction to the database
.rollback()   #causes the db to roll back to the start of pending transaction
.close()      #closes the connection

#Cursor
.callproc()
.execute()
.executemany()
.fetchone()
.fetchmany()
.fetchall()
.nextset()
.arraysize()
.close()

#SQL LITE EXAMPLE
####################################################################################################
import sqlite3
connection = sqlite3.connect('DATABASE.db')
cursor = connection.cursor()

#Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor.execute(table)

#Insert data
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Jar', 'Criss', 'Katowice', 'PL')''')

#Query data
cursor.execute('SELECT * FROM INSTRUCTOR;')

print("All the data")
output_all = cursor.fetchall()
for row_all in output_all:
  print(row_all)
  
#Retrieve data into pandas
import pandas as pd
df = pd.read_sql_query("SELECT * FROM INSTRUCTOR;", connection)

connection.close()
