#http://pythonscraping.com/code

from urllib.request import urlopen
#html = urlopen("http://pythonscraping.com/pages/page1.html")
html = urlopen("http://ithappens.me/story/3")
print(html.read())