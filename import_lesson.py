# from simplecrypt import encrypt, decrypt
# with open("C:\Users\79537\Downloads\encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
import requests,re

# res=requests.get("https://i.ytimg.com/vi/FKrehdxbTOA/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAuyKn3A5BREQcms3l664PMoEnPow")
# print(res.status_code)
# print(res.headers['Content-Type'])
# with open("C:/Users/79537/Downloads/picture.png","wb") as f:
#     f.write(res.content)




# B="<a href="+b+">"
# k=res.content.find(B)
# print("YES") if k!=-1 else print("No")
u_1,u_2=str(input()),str(input())
url=requests.get(u_1)
line=url.text
#print(line)
pattern=r"\bhref=\"(\w+)\1\">\b"
mass=re.findall(pattern, line)
print(mass)
