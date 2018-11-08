import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_81838.xml' #input("Enter -")
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
values = []
for item in counts:
    num = item.text
    numint = int(num)
    #print(numint)
    values.append(numint)
print('Retrieved', len(data), 'characters')
print('Count: ', len(values)) 
print('Sum: ', sum(values))   

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)