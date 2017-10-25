from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
"""html = urlopen("http://bash.im/")"""
print(html.read())