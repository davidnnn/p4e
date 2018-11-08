from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_81836.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numbers = []
# Retrieve all of the tags
tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    numbers.append(number)
print(sum(numbers))