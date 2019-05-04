from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ithappens.me/story/40")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("div", {"class":"text"})
for name in nameList:
    print(len(nameList))
    print(name.get_text())