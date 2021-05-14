from urllib.request import urlopen
url='https://www.google.co.in/'
file_handle=urlopen(url)

from bs4 import BeautifulSoup
soup=BeautifulSoup(file_handle,"html.parser")
print(soup.title.string)

allink=soup.find_all("a")
count=0
for link in allink:
    #print(link.get("href"))
    count+=1
print("number of 'a' tag used=",count)

allink=soup.find_all("style")
counts=0
for link in allink:
    #print(link.get("href"))
    counts+=1
print("number of 'style' tag used=",counts)

allink=soup.find_all("div")
coun=0
for link in allink:
    #print(link.get("href"))
    coun+=1
print("number of 'div' tag used=",coun)

allink=soup.find_all("head")
cou=0
for link in allink:
    #print(link.get("href"))
    cou+=1
print("number of 'head' tag used=",cou)

allink=soup.find_all("span")
co=0
for link in allink:
    #print(link.get("href"))
    co+=1
print("number of 'span' tag used=",co)

allink=soup.find_all("body")
c=0
for link in allink:
    #print(link.get("href"))
    c+=1
print("number of 'body' tag used=",c)

allink=soup.find_all("script")
counte=0
for link in allink:
    #print(link.get("href"))
    counte+=1
print("number of 'script' tag used=",counte)

allink=soup.find_all("html")
counted=0
for link in allink:
    #print(link.get("href"))
    counted+=1
print("number of 'html' tag used=",counted)
print("number of total tags used=",count+counts+coun+cou+co+c+counte+counted)
