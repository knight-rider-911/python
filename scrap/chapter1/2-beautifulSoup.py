from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
html = urlopen("http://ithappens.me/story/40")

bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)
print(bsObj.p)
