import re

import requests
from bs4 import BeautifulSoup
d={}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.821 Yowser/2.5 Safari/537.36"
}
url="https://www.fl.ru/projects/5035938/rasparsit-zagolovki-tovarov-na-python.html"
res=requests.get(url,headers=headers)
res=res.text

soap=BeautifulSoup(res,features="html.parser")

description=soap.find('div',{'class':"b-layout__txt b-layout__txt_padbot_20"})
pattern="«(\w+)»\1"
# str=re.search(pattern,description)
# print(str)

####
text="Наручные часы CASIO MTP-V004L-1B"
txt=re.findall(r"([А-я]+)(\1)\b(\w+)(\2)\b(\w+)(\3)",text)
print(txt)