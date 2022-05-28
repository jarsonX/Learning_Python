#HTTP USING THE REQUESTS LIBRARY IN PYTHON
#Allows to send HTTP requests and download a webpage.

#REQUESTS MODULE BASICS
############################################################

import requests
url = 'https://www.ibm.com/'

r = requests.get(url)
r.status_code
r.request.headers
r.request.body
header = r.headers  #response headers, retrieved as a dict
header['date']  #when request was sent
header['Content-Type']
r.encoding
r.text[:]  #dispalys HTML in the body

#GET REQUEST WITH URL PARAMETERS
############################################################
#Enables to send data to a server and modify query results.

#Construction

#Base url:          httbin.org
#Route:             /get

#Start of query:    ?
#Parameter name:    name
#=
#Value:             Joseph
#&
#Parameter name:    ID
#=
#Value:             123

#>>> http://httpbin.org/get? name=Joseph&ID=123

#EXAMPLE
url_get = 'http://httpbin.org/get'
payload = {'name': 'Joseph', 'ID': '123'}

r_get = requests.get(url_get, params = payload)

print('GET RESULTS')
print(r_get.url)
print(r_get.request.body)
print(r_get.status_code)
print(r_get.text[0:100])
print(r_get.headers['Content-Type'])
print(r_get.json())
print(r_get.json()['args'])
print('--------------------------------------------------\n')

#POST REQUEST
############################################################
#It's sends data to a server just like GET, but the data is
#included in a request body rather than url.

url_post = 'http://httpbin.org/post'
payload = {'name': 'Joseph', 'ID': '123'}  #the same as above

r_post = requests.post(url_post, data = payload)

print('POST RESULTS')
print(r_post.url)
print(r_post.request.body)
print(r_post.status_code)
print(r_post.text[0:100])
print(r_post.headers['Content-Type'])
print(r_post.json())
print(r_post.json()['args'])
print('--------------------------------------------------\n')
