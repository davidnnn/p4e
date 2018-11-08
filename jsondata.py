import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter location: ')
if len(serviceurl) <= 1:
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_81839.json'

print('Retrieving', serviceurl)
uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()

info = json.loads(data)
print('Retrieved', len(info), 'parent objects')
commentcounttotal = 0
commenters = 0
for item in info['comments']:
    # print('Name:', item['name'],\
    # '\nComment Count', item['count'])
    commentcounttotal = commentcounttotal + item['count']
    commenters = commenters + 1

print('Count: ', commenters)
print('Sum: ', commentcounttotal)