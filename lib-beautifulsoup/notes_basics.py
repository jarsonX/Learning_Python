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
#!pip install requests==2.26.0

#Modules
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#Downloading a page in steps:
url = "www.jarson.com"
data = requests.get(url).text  #this returns the html code
data_as_soup_object = BeautifulSoup(data, "html.parser")

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

#Note: to go down a table, we would use .td rather than .b!

#Parent (goes one level up the tree)
parent_tag = tag_child.parent  #<h3><b id="boldest">Lebron James</b></h3>

#Sibling (a paragraph element)
sibling_1 = tag_object.next_sibling  #<p> Salary: $ 92,000,000 </p>
sibling_2 = sibling_1.next_sibling  #<h3> Stephen Curry</h3>
sibling_3 = sibling_2.next_sibling  #and so on.

#HTML ATTRIBUTES
###############################################################################
tag_child.attrs  #list of attributes
tag_child['id']  #accessing an attribute (dictionary-like approach)
tag_child.get('id')  #accessing an attribute by get method

#NAVIGABLE STRING
###############################################################################
#A class that contains string from a tag (type NavigableString), similar to
#a Python string, but also supports some BeautifulSoup features.
tag_string = tag_child.string  #'Lebron James'

#FIND ALL FILTER AND ITERATION THROUGH RESULTSET
###############################################################################
#Looks through a tag’s descendants and retrieves all that match filters.

#Syntax: bs_object.find_all(name, attrs, recursive, string, limit, **kwargs)
#Note: there is also bs_object.find() method.

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
#tags with that name and its children. The result is a list-like ResultSet and
#it's iterable just like any list.
table_rows = table_bs.find_all('tr')
first_row = table_rows[0]

#This is a table, so to obtain a child we use .td rather than .b, i.e. first_row.td

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

#CASE: FIND THE SECOND TABLE
###############################################################################
#Consider html containing two tables:

'''%%html
<h3>Rocket Launch </h3>

<p>
<table class='rocket'>
  <tr>
    <td>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Florida </td>
    <td>80 kg</td>
  </tr>
</table>
</p>
<p>

<h3>Pizza Party  </h3>
  
    
<table class='pizza'>
  <tr>
    <td>Pizza Place</td>
    <td>Orders</td> 
    <td>Slices </td>
   </tr>
  <tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td >144 </td>
  </tr>
  <tr>
    <td>Papa John's </td>
    <td>15 </td>
    <td>165</td>
  </tr>
  '''

two_tables = "<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

#Finding any first element is easy:
first_t = two_tables_bs.find("table")

#Finding the second element is a bit tricky, because we need more details to narrow down the search, like a specific class.
second_t = two_tables_bs.find("table", class_ = "pizza")  #an underscore ("_") is needed, because "class" is a keyword in Python

#CASE: SCRAPE ALL LINKS
###############################################################################
url = "http://www.ibm.com"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
for link in soup.find_all('a', href=True):  #in html link is represented by the tag <a>
      print(link.get('href'))
