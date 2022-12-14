import requests
import json

client_id = '759d1a1afdc0b19632c1'
client_secret = '1b1d5b3f46875e76d1971a1b2f2fc499'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

params={
    "templated":True
}
d={}
with open(r'C:/Users/79537/Downloads/dataset_24476_4.txt',encoding="UTF-8") as file:
    while True:
        str = file.readline().split()
        if not str:
            break
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/{}".format(*str), headers=headers, params=params)
        # разбираем ответ сервера
        j = json.loads(r.text)
        d[j["sortable_name"]]=j['birthday']
d=sorted(d,key=lambda x:d[x])
with open(r'C:/Users/79537/Downloads/solve.txt',"w",encoding="UTF-8") as final:
    for i in d:
        final.write(i + "\n")