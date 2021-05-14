from pyexcel_xls import save_data
from pyexcel_xls import read_data
from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter
import json

d=read_data("Book1.xlsx")  
s=json.dumps(d)
obj=json.loads(s)
#for k in obj:
#    print(obj[k][0][0])
#urlNames=dict()
wb=xlsxwriter.Workbook('Book2.xlsx') 
for k in obj:
    worksheet=wb.add_worksheet(str(k))
    worksheet.write("A1",obj[k][0][0])
    worksheet.write("A3","WORDS")
    worksheet.write("B3","COUNT")
    chart=wb.add_chart({'type':'column'})
    req=urllib.request.Request(str(obj[k][0][0]),data=None,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    f=urllib.request.urlopen(req)
    s=f.read().decode('utf-8')
  
    soup=BeautifulSoup('https://kerala.gov.in/web/guest/gallery',"html.parser")
    for script in soup(["script","style"]):
        print(script.extract())
    t=soup.get_text()
    text = "".join([s for s in t.splitlines(True) if s.strip("\r\n")])
    L=text.split()
    wor=[]
    for i in range(1,len(obj[k])):
        wor.append(obj[k][i][0])
        
           
    words=sorted(set(wor))
    countD=dict()
    i=3
    for w in words:
       countD[w]=L.count(w)
       worksheet.write(i,0,w)
       worksheet.write(i,1,L.count(w))
       i=i+1
    area="="+str(k)+"!$B$4:$B$"+str(i)     
    cate="="+str(k)+"!$A$4:$A$"+str(i)
    chart.add_series({'categories':cate ,'values': area})
    chart.set_title({'name': 'WORD COUNT'})
    chart.set_x_axis({'name': 'Words'})
    chart.set_y_axis({'name': 'Count'})
    chart.set_style(37)
    worksheet.insert_chart("F4",chart)
    print(countD)
    
wb.close()    
