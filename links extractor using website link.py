from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = input('Enter the link to extract attached links: ')
y = urllib.request.urlopen(x,context=ctx).read()
z = BeautifulSoup(y,'html.parser')
tags = z('a')
for a in tags:
    print(a.get('href',None))
