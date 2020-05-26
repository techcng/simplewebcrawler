# very basic python link crawler

from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

url = input('Enter url :')
html = urlopen(url).read()
soup = BS(html, 'html.parser') #can be use lxml insted of html.psrser

tags = soup('a')
for tag in tags:
    print(tag.get('href'))
