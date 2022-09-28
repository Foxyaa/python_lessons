import requests
url="http://numbersapi.com/{}/math?"
params={
    "json":"true"
}
with open(r'C:/Users/79537/Downloads/dataset_24476_3.txt') as file, open(r'C:/Users/79537/Downloads/fin.txt',"w") as fin:
    while True:
        num=file.readline().split()
        if not num:
            break
        print(url.format(*num))
        res = requests.get(url.format(*num),params=params)
        data = res.json()
        if data["found"] is False:
            fin.write("Boring\n")
            print("Boring")
        else:
            fin.write("Interesting\n")
            print("Interesting")



