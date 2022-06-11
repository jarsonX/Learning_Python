#DB-API CODE SCHEME
####################################################################################################

from dbmodule import connect

connection = connect ('databasename', 'username', 'pswd')  #connection object
cursor = connection.cursor()  #cursor object

cursor.execute('select * from tablename')  #run queries
results = cursor.fetchall()

cursor.close()
connection.close()  #free resources
