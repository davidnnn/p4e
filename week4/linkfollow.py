import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Laia.html'
num = input('Enter count: ')
position = input('Enter position: ')
print('Retrieving: ', url)
for i in range(int(num)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving: ', tags[int(position)-1].get('href', None))
    url = tags[int(position)-1].get('href', None)