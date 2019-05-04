from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
html = urlopen("https://ithappens.me/story/9191")

bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("div",{"class":"text"}).children:
    print(child)