#An example of how to load file by HTTP method GET

import requests
import os 
from PIL import Image
##from IPython.display import IFrame

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)

print(r.headers)  #checking headers
print(r.headers['Content-Type'])  #checking type

#An image is a response object that contains the image as a bytes-like object. 
#As a result, we must save it using a file object. 
#First, we specify the file path and name:

path=os.path.join(os.getcwd(),'image.png')
print(path)

#In order to access the body of the response, we use the attribute content.
#Then save it using the open function and write method:
    
with open(path,'wb') as f:
    f.write(r.content)
    
Image.open(path)