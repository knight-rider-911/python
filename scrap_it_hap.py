from urllib.request import urlopen
from bs4 import BeautifulSoup

str_http='https://ithappens.me/story/'
res_str_http=''
f = open('d:/test_python.csv', 'w')
for http_str in range (1,10):
    res_str_http=str_http+str(http_str)
    f.write(res_str_http+';')
    print(res_str_http)
    f.write('"')
    html = urlopen(res_str_http)
    bsObj = BeautifulSoup(html, "html.parser")
    for child in bsObj.find("div",{"class":"text"}).children:
        print(child)
        f.write(str(child))
    f.write('"'+'\n')

f.close()