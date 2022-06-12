#DB-API CODE SCHEME
####################################################################################################
import <<<appropriate module>>>

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
cursor.execute('''insert into INSTRUCTOR values (1, 'Jar', 'Criss', 'Katowice', 'PL')''')

#Query data
cursor.execute('SELECT * FROM INSTRUCTOR;')

print("All the data")
output_all = cursor.fetchall()
for row_all in output_all:
  print(row_all)
  
#Retrieve data into pandas
import pandas as pd
df = pd.read_sql_query("SELECT * FROM INSTRUCTOR;", connection)

cursor.close()
connection.close()

#SQL SERVER EXAMPLE
####################################################################################################
import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=<<<SERVER_NAME>>>;DATABASE=<<<DB_NAME>>>;Trusted_Connection=yes;')
cursor = connection.cursor()

#Query data
cursor.execute('SELECT CategoryID, CategoryName, Description FROM Categories')

output_all = cursor.fetchall()
for row_all in output_all:
  print(row_all)

#Retrieve data into pandas
import pandas as pd
#pd.set_option("display.max_rows", 10, "display.max_columns", 3) 
df = pd.read_sql_query('SELECT CategoryID, CategoryName, Description FROM Categories', connection)  

print(df)

#Save to csv
df.to_csv(r'C:\Users\username\Desktop\example.csv')

cursor.close()
connection.close()
