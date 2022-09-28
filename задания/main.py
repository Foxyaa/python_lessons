def z1():
    with open(r"C:\Users\79537\Downloads\01.txt") as file:
        k = 0
        operations = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y}
        while True:
            line = file.readline().strip()
            if not line:
                break
            oper, num = line[0], int(line[1:])
            print(oper, "*****", num)
            k = operations[oper](k, num)
        print(k)
def z2():
    with open(r"C:\Users\79537\Downloads\02.txt") as file:
        b2,b3=0,0

        d,str={},""
        while True:
            flag, f = False, False
            line = file.readline().strip()
            if not line:
                break
            for x in line:
                if x not in str:
                    d[x]=1
                    str+=x
                else:
                    d[x]+=1
            print(d)
            for k in d.values():
                if k==3 and flag == False:
                    b3+=1
                    flag=True
                if k==2 and f == False:
                    b2+=1
                    f=True
            d, str = {},""
        print(b2, "*", b3, "=", b3 * b2)
def z5():
    with open(r"C:\Users\79537\Downloads\05.txt") as file:
        s=file.readline().strip()
        f = True
        while f:
            k = s[0]
            str = s
            for i, b in enumerate(s[1:]):
                if b != k and b.lower() == k.lower():
                    s = s[:i] + s[i + 1:]
                    s = s[:i] + s[i + 1:]
                    break
                    # b = s[1]
                else:
                    k = b
            if str == s:
                f = False
    print(s, " ", len(s))
import copy

def z6():
    d0,d1,d2,d3,d4,d5,d6,d7={},{},{},{},{},{},{},{}
    with open(r"C:\Users\79537\Downloads\06.txt") as file:
        str=""
        while True:
            line = file.readline().strip()
            if not line:
                break
            #0
            if line[0] not in d0:
                d0[line[0]] = 1
            else:
                d0[line[0]] += 1
            #1
            if line[1] not in d1:
                d1[line[1]] = 1
            else:
                d1[line[1]] += 1
            #2
            if line[2] not in d2:
                d2[line[2]] = 1
            else:
                d2[line[2]] += 1
            #3
            if line[3] not in d3:
                d3[line[3]] = 1
            else:
                d3[line[3]] += 1
            #4
            if line[4] not in d4:
                d4[line[4]] = 1
            else:
                d4[line[4]] += 1
            #5
            if line[5] not in d5:
                d5[line[5]] = 1
            else:
                d5[line[5]] += 1
            #6
            if line[6] not in d6:
                d6[line[6]] = 1
            else:
                d6[line[6]] += 1
            #7
            if line[7] not in d7:
                d7[line[7]] = 1
            else:
                d7[line[7]] += 1
        lst=[d0,d1,d2,d3,d4,d5,d6,d7]
        # print(d0)
        # print(d1)
        # print(d2)
        # print(d3)
        # print(d4)
        # print(d5)
        # print(d6)
        # print(d7)

        for d in lst:
            mx = list(d.values())[0]
            mx_key = list(d.keys())[0]
            for key, j in d.items():
                if j > mx:
                    mx = j
                    mx_key = key
            str += mx_key
        print(str)
import re
def z7():
    count = 0
    with open(r"C:\Users\79537\Downloads\07.txt") as file:
        while True:
            str = file.readline().strip()
            if not str:
                break
            # str = "aaaa[qwer]tyui"  # не проходит проверку с одиннаковыми буквами
            # str="ioxoj[josdfgh]zxvccvbn"
            f = False
            flag = True
            k = 1
            for i in range(len(str)-3):
                if k == 0:
                    break
                if str[i] == "[":
                    flag = False
                    continue
                if str[i] == "]":
                    flag = True
                    continue
                if str[i] == str[i+3] and str[i+1] == str[i+2] and str[i] != str[i+1]:
                    if flag:
                        f = True
                    else:
                        f = False
                        k = 0
                        break
            if f:
                count += 1
    print(count)

import gc #4021032+76280+47738+691015+543197082=548033147
def z9():
    with open(r"C:\Users\79537\Downloads\09.txt") as file, open(r"C:\Users\79537\Downloads\09_output.txt","w") as output:
        while True:
            s = file.readline().strip()
            if not s:
                break
            i = 0
            # s = "(10x11)(12x144)jk op\nX(8x2)(3x3)ABCY"
            while i < len(s):
                if s[i]==" ":
                    i += 1
                    continue
                if s[i] == "(" and s[i + 1].isdigit():
                    y=i
                    while True:
                        if s[y]=="x":
                            index=y
                            break
                        y+=1
                    num=s[i+1:index]
                    while True:
                        if s[y]==")":
                            end=y
                            break
                        y+=1
                    word=s[end+1:end+1+int(num)]
                    digit=s[index+1:end]
                    output.write(unzip(word, int(digit)))
                    i += len(word) + 3 + len(num) + len(digit)
                    gc.collect()
                else:
                    output.write(s[i])
                    i += 1


def unzip(x,y): #x-последовательность символов, y-количество раз для повторения
    str=""
    for _ in range(int(y)):
        str += x
    return str

def result():
    with open(r"C:\Users\79537\Downloads\10_output.txt") as f:
        res = f.readline().strip()
        print(len(res))


def z3():
    N=[["_","_","D"],#1
    ["_","_","R","_","_","D"],#2
    ["U","L","_","R","_","_","D"],#3
    ["_","_","L","_","_","_","_","D"],#4
    ["_","_","_","_","_","R"],#5
    ["_","U","_","_","L","_","R","_","_","D"],#6
    ["_","_","U","_","_","L","_","R","_","_","D"],#7
    ["_","_","_","U","_","_","L","_","R","_","_","D"],#8
    ["_","_","_","_","_","_","_","L"],#9
    ["_","_","_","_","_","U","_","_","_","_","R"],#A
    ["_","_","_","_","_","_","U","_","_","L","_","R","D"],#B
    ["_","_","_","_","_","_","_","U","_","_","L"],#C
    ["_","_","_","_","_","_","_","_","_","_","U"]]#D

    with open(r"C:\Users\79537\Downloads\03.txt") as file, open(r"C:\Users\79537\Downloads\03_output.txt","w+") as output:
        el = N[4]
        num = 4
        while True:
            s = file.readline().strip()
            if not s:
                break
            for char in s:
                for w in el:
                    if w == char:
                        num = el.index(w)
                        el = N[num]
                        break
            if num==9:
                num="A"
            elif num==10:
                num="B"
            elif num==11:
                num="C"
            elif num==12:
                num="D"
            else:
                num+=1
            # print("***",num,"***")
            output.write(str(num))
        res = output.readline().strip()
        print(res)


def z8():
    import re
    with open(r"C:\Users\79537\Downloads\08.txt") as file:
        a=50
        b=6
        plate=[["."] * a for _ in range(b)]
        while True:
            s = file.readline().strip()
            if not s:
                break
            nums = re.findall(r'\d+', s)
            nums = [int(i) for i in nums]
            if re.match(r"rotate column", s):
                lst=[]
                for i in range(b):
                    lst.append(plate[i][nums[0]])
                for i in range(nums[1]):
                    lst.insert(0, lst.pop())
                for i in range(b):
                    plate[i][nums[0]]=lst[i]

            elif re.match(r"rotate row", s):
                plate=shift(plate,nums)
            elif re.match(r"rect", s):
                for i in range(nums[1]):
                    for y in range(nums[0]):
                        plate[i][y]="#"
    for k in range(b):
        print(plate[k])
    count=0
    for i in range(b):
        for j in range(a):
            if plate[i][j]=="#":
                count+=1
    print(count)
def shift(plate,nums):
    for i in range(nums[1]):
        plate[nums[0]].insert(0, plate[nums[0]].pop())
    return plate

#задание 10
def findCompression(str):
    length=0
    i=0
    while i<len(str):
        if str[i] == "(":
            other=i
            while str[other]!=")":
                other+=1
            info=list(map(int,str[i+1:other].split('x')))
            stringRange=str[other+1:other+info[0]+1]
            length+=info[1]*findCompression(stringRange)
            i+=other-i+info[0]
        else:
            length+=1
            i+=1
    return length


def z4():
    sum=0
    with open(r"C:\Users\79537\Downloads\04.txt") as file:
        rooms = file.read().strip().split("\n")
    for i in range(len(rooms)):
        tokens=rooms[i].split("-")
        sectorID=int(tokens[len(tokens)-1].split("[")[0])
        neededLetters=tokens[len(tokens)-1].split('[')[1].replace(']', '')
        allLetters=[]
        for i in range(len(tokens)-1):
            for j in tokens[i]:
                allLetters+=j
        counts={}
        for j in range(len(allLetters)):
            if allLetters[j] not in counts.keys():
                counts[allLetters[j]]=0
            counts[allLetters[j]]+=1
        counts=dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))
        keys=list(counts.keys())
        if "".join(keys[0:5])==neededLetters:
            sum+=sectorID
    return sum
