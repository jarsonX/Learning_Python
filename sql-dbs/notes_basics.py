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
conn = sqlite3.connect('DATABASE.db')
cursor_obj = conn.cursor()

#Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)

#Insert data
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Jar', 'Criss', 'Katowice', 'PL')''')

#Query data
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)
  
#Retrieve data into pandas
import pandas as pd
df = pd.read_sql_query("select * from instructor;", conn)

conn.close()
