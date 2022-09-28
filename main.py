# def main():
#
# main()
# num=[int(i) for i in input().split()]
# num.sort()
# res,k=0,num[0]
# for n in range (len(num)):
#     if num[n]==k:
#         res+=1
#     elif res>1:
#         print(num[n-1], end=' ')
#         res,k=0, num[n+1]
#     else:
#         continue


# num=[int(i) for i in input().split()]
# num.sort()
# sp=[num[0]]
# for i,n in enumerate(num):
#     if n==sp:
#         sp.append(n)
#     elif len(sp)>2:
#         print(sp[0], end=' ')
#         sp=[i+1]
#     else:
#         continue


# s=[int(i) for i in input().split()]
# res=0
# for i in range (len(s)):
#     if s[i]==s[i+1]:
#         res+=1
#     else:
#         print(s[i], end='')
#         res=0
def z():  # раскодирование строки из файла и запись вывода в другой файл
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    num = ""
    with open(r'C:/Users/79537/Downloads/dataset_3363_2.txt') as inf, \
            open(r'C:/Users/79537/Downloads/final_out.txt', "w") as outf:
        s = inf.readline().strip() + "#"
        for i, n in enumerate(s):
            if n not in numbers:
                b = s[i]
            else:
                num += s[i]
                if s[i + 1] not in numbers:
                    outf.write(b * int(num))
                    num = ""


# with open(r'C:/Users/79537/Downloads/dataset_3363_2.txt') as infile:
#     lst = infile.read().replace('\n', '').replace('\r', '').lower().split()
#     x, d = [], {}
#     for i in lst:
#         if i not in x:
#             # print(i,lst.count(i))
#             d[lst.count(i)] = i
#     for j,n in enumerate(d.keys()):
#         if j==0 or n>d[]:
#             res=
#         elif j==j-1:

# with open('C:/Users/79537/Downloads/marks.txt',"r",encoding='utf-8') as fi, open(r'C:/Users/79537/Downloads/out.txt', "w") as outfi:
#     medium_1, medium_2, medium_3, count_str = 0, 0, 0, 0
#     while True:
#         line = fi.readline().split(';')
#         count_str += 1
#         medium_ab = (int(line[1])+int(line[2])+int(line[3]))/3
#         ab=str(medium_ab)+"\n"
#         outfi.write(ab)
#         medium_1 +=int(line[1])
#         medium_2 +=int(line[2])
#         medium_3 +=int(line[3])
#     print(medium_1)
#     outfi.write(medium_1/count_str,medium_2/count_str,medium_3/count_str)


# lst2,final=[],[]
# lst=[int(i) for i in input().split()]
# lst.sort()
# for i in lst:
#     if i in lst2 and i not in final:
#         final+=[i]
#     elif i not in lst2:
#         lst2+=[i]
# print(*final,end=' ')


from operator import itemgetter


def my_words(path):  # самое частое слово в файле
    with open(path, "r", encoding='cp1251') as ifile, open(
            'C:/Users/79537/Downloads/dataf.txt', "w") as ofile:
        x, d, n = [], {}, 0
        lst = ifile.read().lower().split()
        for i in lst:
            if i not in x:
                d[i] = lst.count(i)
                x += [i]
        for i in sorted(sorted(d.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True):
            print(*i, file=ofile)
            break


# my_words('C:/Users/79537/Downloads/voyna-i-mir-tom-1.txt')

def pfile():
    with open('C:/Users/79537/Downloads/voyna-i-mir-tom-1.txt', "r") as f:  # для информации о кодировке
        print(f)


# key,value,s,r=input(),input(),input(),input()
# print(s.translate(s.maketrans(key,value)))
# print(r.translate(r.maketrans(value,key)))

# mas=[0,0]
# n=int(input())
# for i in range(n):
#     s=input().split(" ")
#     s[1]=int(s[1])
#     if s[0]=="север":
#         mas[1]+=s[1]
#     elif s[0]=="запад":
#         mas[0]-=s[1]
#     elif s[0] == "восток":
#         mas[0] += s[1]
#     elif s[0] == "юг":
#         mas[1] -= s[1]
# print(*mas)

def fib(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
    return (b)


# n = int(input())
# print(fib(n))

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)


# a, b = map(int, input().split())
# print(gcd(a, b))
def con():  # конструкция как писать короче
    a = int(input())
    print("True" if -15 < a <= 12 or 14 < a < 17 or 19 <= a else "False")


def acg():
    d = {}

    def add(nmspc, arg):
        d[nmspc] += arg

    def get(nmspc, arg):
        if d[nmspc] == arg:
            print(nmspc)
        elif d["global"] == arg:
            print("None")
        else:
            get(d.get(nmspc), arg)

    def create(nmspc, arg):
        d[arg] = nmspc

    n = int(input())
    for i in range(n):
        cmd, nmspc, arg = input().split()
        if cmd == "get":
            get(nmspc, arg)
        elif cmd == "add":
            add(nmspc, arg)
        elif cmd == "create":
            create(nmspc, arg)


# import csv, re
# with open(r"C:\Users\79537\Downloads\Crimes.csv") as f:
#     r = csv.DictReader(f)
#     for row in r:
#         if re.search(r"\d\d/\d\d/[2015]", row["Date"]) == True:
#             print('YES')

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)


##################
class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                if f(i) is True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


############
import math
from itertools import takewhile
import itertools


def primes():
    a = 2
    while True:
        if (math.factorial(a - 1) + 1) % a == 0:
            yield a
        a += 1


def reverse_file():
    with open(r"C:\Users\79537\Downloads\dataset_24465_4 (1).txt", encoding='cp1251') as f, open("output.txt", "w",
                                                                                                 encoding='cp1251') as result:
        result.write("".join(f.readlines()[::-1]))


import \
    os.path  # import shutil shutil.copy("file1","file2") shutil.copytree("dir1","dir2") - библиотека копирует файла и директории, os.walk


def path_file():  # выводит абсолютный путь
    print(os.path.abspath("main.py"))


"""
методы строки
s[start:end].startswith(str) - проверяет начинается ли строка со строки, переданной в аргумент
В аргумент можно передать префикс;
endswith() - проверяет заканчивается ли строка со строки, переданной в аргумент;
s[start:end].find(str) - индекс первого вхождения, если нет вернет -1;
s.index(str) - индекс первого вхождения, если нет ValueError;
count()
"""

"""
s, a, b, i = [input() for _ in range(3)] + [0]
f = True
if a in b and a in s:
    print("Impossible")
    f = False
while f:
    if a in s:
        s = s.replace(a, b)
        i += 1
    else:
        if i > 1000:
            print("Impossible")
        else:
            print(i)
        f = False
"""
def Seacrh():
    s, t, count = [str(input()) for _ in range(2)] + [0]
    for i in range(len(s)):
        i = s[i:i + len(t)].find(t)
        if i == -1:
            continue
        count += 1
    print(count)

import sys,re
def parse():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r"(\w)(\1)+"
        line = re.sub(pattern, r'\1', line)
        print(line)

def solution():
    x = input().split()
    lst,k=[],[]
    for i in x:
        if i.isalpha():
            lst+=[i]
        else:
            lst.clear()
        if len(lst)==2:
            k+=[lst]
            lst=[]
    if len(k)==0:
        print("Мало слов!")
    else:
        for i in k:
            print(*i)

# k,m=map(int,input().split())
# mass=[]
# mass += list(map(int,input().split()))
# print(mass)

def flippingBits(n):
    res=""
    n=format(n,'b')
    b_dict={"0":"1","1":"0"}
    if len(n)<32:
        res+="1"*(32-len(n))
    for i in n:
        res+=b_dict[i]
    return int(res,2)
print(flippingBits(1))