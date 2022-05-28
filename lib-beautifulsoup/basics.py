#FUNDAMENTALS
###############################################################################

#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#In case of HTML, this is accomplished by representing the HTML as a set of 
#objects with methods used to parse the HTML. We can navigate the HTML as 
#a tree and/or filter out what we are looking for.

#In order to webscrap with BeautifulSoup, it is necessary to first download
#a page using requests module.

#Install libraries, if needed
#!mamba install bs4==4.10.0 -y
#!pip install lxml==4.6.4
#!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

#Modules
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#An example page
#Normally, we would need to download it using requests module.

'''HTML Example 1
%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
'''

#Store it as a string
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

#SOUP OBJECT
###############################################################################

#Beautiful Soup transforms a complex HTML document into a complex tree of 
#Python objects, i.e. a nested structure.

soup = BeautifulSoup(html, "html.parser")

#Display the object
print(soup.prettify())

#TAG
###############################################################################

#Let's say we want the title of the page and the name of the top paid player.
#The Tag object corresponds to an HTML tag in the original document, 
#for example, the tag title.

#Example of Tag
tag_example = soup.title  #<title>Page Title</title>

#If there is more than one Tag with the same name, the first element with that 
#Tag name is called.
tag_object = soup.h3  #<h3><b id="boldest">Lebron James</b></h3>

#CHILDREN, PARENTS, SIBLINGS
###############################################################################

#Children (goes one level down the tree)
tag_child = tag_object.b  #<b id="boldest">Lebron James</b>

#Parent (goes one level up the tree)
parent_tag = tag_child.parent  #<h3><b id="boldest">Lebron James</b></h3>

#Sibling (a paragraph element)
sibling_1 = tag_object.next_sibling  #<p> Salary: $ 92,000,000 </p>
sibling_2 = sibling_1.next_sibling  #<h3> Stephen Curry</h3>
sibling_3 = sibling_2.next_sibling  #and so on.

#HTML ATTRIBUTES
###############################################################################

tag_child.attrs  #list of attributes
tag_child['id']  #accessing an attributes
tag_child.get('id')  #accessing content of the atrribute

#NAVIGABLE STRING
###############################################################################

#A class that contains string from a tag (type NavigableString), similar to
#a Python string, but also supports some BeautifulSoup features.
tag_string = tag_child.string  #'Lebron James'

#FIND ALL FILTER AND ITERATION THROUGH RESULTSET
###############################################################################
#Looks through a tag’s descendants and retrieves all descendants that match 
#filters.

#Syntax: find_all(name, attrs, recursive, string, limit, **kwargs)

'''HTML Example 2
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
'''

#Store it as a string and create an object
table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

#Name
############
#When we set the name parameter to a tag name, the method will extract all the 
#tags with that name and its children. The result is a list-like ResultSet.
table_rows = table_bs.find_all('tr')

#We can iterate through ResultSet
for i,row in enumerate(table_rows):
    print("row",i,"is",row)  
    
#Find_all can be applied to cells
for i,row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")
    for j,cell in enumerate(cells):
        print("column",j,"cell",cell)
        
#Iteration can also be based on a list
list_input = table_bs.find_all(name=["tr", "td"])

#Attributes
############
#Filter can be based on attributes, like 'id'.

#All elements with id flight
table_bs.find_all(id="flight")

#All elements that have href attribute (content is not important)
table_bs.find_all(href=True)

#All elements that have links to the Florida Wikipedia page
list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")

#Strings
############
#Search for strings instead of tags. 

#Finds all the elments with "Florida"
table_bs.find_all(string="Florida")

#FIND
###############################################################################

#Finds the first element in the document.

#Syntax: find(name, attrs)
