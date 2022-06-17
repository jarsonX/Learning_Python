#DATA ENGINEERING PROCESS / ETL

#Note: importing of modules might be repaeated for illustration purposes.

#FUNDAMENTALS
##############################################################################
#File format is a standard in which data is encoded. It specifies whether the
#file is a binary or ASCII file and shows how information is organized.

#Process of converting an object into a special format which is suitable for
#transmitting over the network or storing in file or database is called
#serialization (pol. serializacja)

#Reverse of serialization, i.e. converting the special format returned by the 
#serialization back into a usable object is called deserialization.

#READ/SAVE
##############################################################################

#Data format        Read                  Save
#csv                pd.read_csv()         df.to_csv()
#json               pd.read_json()        df.to_json()
#excel              pd.read_excel()       df.to_excel()
#xml                pd.read_xml()         df.to_xml()
#hdf                pd.read_hdf()         df.to_hdf()
#sql                pd.read_sql()         df.to_sql()

#read_excel supports xls, xlsx, xlsm, xlsb, odf, ods and odt

#COMMA-SEPARATED VALUES (CSV)
##############################################################################
#A spreadsheet file format where data is stored in cells. Each cell is
#organized in rows and columns. Columns can be of different types.
#A separate line is commonly referred to as a record.

#LOAD
############################
import pandas as pd

df = pd.read_csv('...\file.csv', header=None)  #load a file to DataFrame

#TRANSFORM
##############
df.columns =['First', 'Second', 'Third']  #add column headers

#      First   Second   Third
# 0     x       x        x
# 1     x       x        x
# 2     x       x        x
# ...

df['First']  #retrieve column as a series
df[['First', 'Second']]  #retrieve column/columns as a separate df

#Slicing by labels
df.loc[0]  #retrieve row; 0 is a label, referring to column index
df.loc[[0,1,2], 'First' ]  #retrieve 0, 1 and 2 rows from first column 

#Slicing by indices
df.iloc[0]  #retrieve row; although it matches label, 0 is an index
df.iloc[[0,1,2], 0]  #retrieve 0, 1 and 2 rows from first column 

#Basic functions
import pandas as pd
import numpy as np

#Creating a df from array
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

#    a b c
# 0  1 2 3
# 1  4 5 6
# 2  7 8 9

df = df.transform(func = lambda x : x + 10)  #add 10 to each element
df = df.apply(func = lambda x : x + 10)  #add 10 to each element

df_sqrt = df.transform(func = ['sqrt'])  #find square root of each element

#For manipulating values, both apply() and transform() can be used to manipulate
#an entire DataFrame or any specific column. But there are 3 differences:

    #(1) Transform() can take a function, a string function, a list of functions, 
        #and a dict. However, apply() is only allowed a function.
    #(2) Transform() cannot produce aggregated results.
    #(3) Apply() works with multiple Series at a time. But, transform() is only 
        #allowed to work with a single Series at a time.

#For working in conjunction with groupby():

    #(1) Transform() returns a Series that has the same length as the input.
    #(2) Apply() works with multiple Series at a time. But, transform() is only 
        #allowed to work with a single Series at a time.
        

#JAVASCRIPT OBJECT NOTATION (JSON)
##############################################################################
#A lightweight data-interchange, language-independent format, easy to read and
#write. The text in JSON is done through string which contains the values in
#key-value mapping (similar to the dictionary in Python).

#LOAD
############################
#Using pandas
import pandas

df = pd.read_json('...\file.json')

#Using json
import json   

with open('file.json', 'r') as input_file: 
    json_object = json.load(input_file)  #reading from json file 

#WRITING JSON TO A FILE (SERIALIZATION)
############################

#Dictionary organised to include in JSON file:
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

#json.dump() can be used for writing to JSON file

with open('file_name.json', 'w') as write_file:
    json.dump(person, write_file)

#json.dumps() helps in converting a dictionary to a JSON object

json_object = json.dumps(person, indent = 4)  #first serializing json
#indent defines the number of units for indentation
  
with open("sample.json", "w") as write_file:  #then writing to file
    write_file.write(json_object) 
    
#To deserialize objects back to the Python object, we use the load() function.

#READING JSON TO A FILE (DESERIALIZATION)
############################
import json 
  
with open('file.json', 'r') as input_file: 
    json_object = json.load(input_file) 

#MICROSOFT EXCEL OPEN XML (XLSX)
##############################################################################
#A spreadsheet file format where data is organized under the cells and columns
#in a sheet. 

#LOAD
############################
import pandas as pd

df = pd.read_excel('...\file.xlsx')

#XML
##############################################################################
#XML is know as Extensible Markup Language. The format is human-readable and
#machine-readable. Pandas does not include any methods to read and write XML
# files. That is why other modules are required.

#xml.etree.ElementTree enables creating and analysing XML documents. It represents
#the data as a tree. We can move across it using nodes which are elements and
#sub-elements of the file.

#WRITING WITH xml.etree.ElementTree
############################
import xml.etree.ElementTree as ET

#Create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElements(details, 'firstname')
second = ET.SubElements(details, 'lastname')
third = ET.SubElement(details, 'age')

first.text = 'Leon'
second.text = 'Michalsky'
third.text = '10'

#Create a new XML file with the results
my_data = ET.ElementTree(employee)
#my_file = open(file.xml, 'wb)  #classic way of writing it
#my_file.write(my_data)
with open('file.xml', 'wb') as output_file:
    my_data.write(output_file)  #this syntax is actually correct

#READING WITH xml.etree.ElementTree
############################
#Read XML data and put it in a Pandas DataFrame.

#The source code of the file, important for understanding how .find() works.
'''
<employees>
    <details>
        <firstname>Shiv</firstname>
        <lastname>Mishra</lastname>
        <title>Engineer</title>
        <division>Computer</division>
        <building>301</building>
        <room>11</room>
    </details> 
    <details>
        <firstname>Yuh</firstname>
        <lastname>Datta</lastname>
        <title>developer</title>
        <division>Computer</division>
        <building>303</building>
        <room>02</room>
    </details> 
    <details>
        <firstname>Rahil</firstname>
        <lastname>Khan</lastname>
        <title>Tester</title>
        <division>Computer</division>
        <building>304</building>
        <room>10</room>
    </details> 
    <details>
        <firstname>Deep</firstname>
        <lastname>Parekh</lastname>
        <title>Designer</title>
        <division>Computer</division>
        <building>305</building>
        <room>14</room>
    </details>
    
</employees>
'''

#Parse an XML file, create a list of columns for DataFrame, extract useful
#information from the XML file and add to the DataFrame.

import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')  #check the source code above
root = tree.getroot()

columns = ['firstname', 'lastname', 'title', 'division', 'building', 'room']

df = pd.DataFrame(columns = columns)

for node in root:
    firstname = node.find('firstname').text
    lastname = node.find('lastname').text
    title = node.find('title').text
    division = node.find('division').text
    building = node.find('building').text
    room = node.find('room').text

    df = df.append(pd.Series([firstname, lastname, title, division, building, \
                              room], index = columns), ignore_index = True)

#READING USING PANDAS.READ_XML
############################
import pandas as pd

df = pd.read_xml('file.xml', xpath="...\...")

#BINARY FILE FORMAT
##############################################################################
#Binary files are any files where the format isn't made up of readable 
#characters. It contain formatting information that only certain applications 
#or processors can understand. While humans can read text files, binary files 
#must be run on the appropriate software or processor before humans can read 
#them.

#Binary files can range from image files like JPEGs or GIFs, audio files like 
#MP3s or binary document formats like Word or PDF.

#READING THE IMAGE FILE
############################
from PIL import Image

img = Image.open('name.jpg')
img.show()
