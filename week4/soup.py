import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page1.htm' #input("Enter -")
html = urllib.request.urlopen(url).read()
o = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
    print(tag.get('href', None))
print(o)