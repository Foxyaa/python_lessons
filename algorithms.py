def z1():
    n, capacity = map(int, input().split())
    d = []
    for _ in range(n):
        price, amount = map(int, input().split())
        k = price / amount
        d.append([k, amount])
    d.sort(reverse=True)
    count = 0
    final_price = 0
    while count < capacity and len(d) != 0:
        if count + d[0][1] > capacity:
            r = capacity - count
            count += r
            final_price += d[0][0] * r
        else:
            count += d[0][1]
            final_price += d[0][0] * d[0][1]
        d.pop(0)
    print(final_price)


def z2():
    n = int(input())
    d = []
    for _ in range(n):
        x, y = map(int, input().split())
        d.append([x, y])
    d.sort()
    s = []
    tck = []
    s.append(d[0])
    count = 0
    flag = False
    for i in range(1, n - 1):
        if s[-1][-1] == d[i][0]:
            count += 1
            s.append(d[i])
            tck.append(d[i][0])
            flag = True
        elif s[-1][-1] < d[i][0]:
            count += 2
            tck.append(s[-1][-1])
            tck.append(d[i][1] - 1)
            s.append(d[i])
            flag = True
    if flag == False:
        count += 1
        tck.append(s[-1][-1])
    print(count)
    print(*tck)


# import queue
#
#
# s=str(input())
# q = queue.PriorityQueue()
# for i in s:
#     q.put(i)

# куча

# lst=[]
# def insert_x(x,lst):
#     lst.append(x)
#     i = lst.index(x) // 2
#     if x > lst[0] :
#         lst.insert(0, lst.pop())
#     else:
#         while x < i:
#             lst.insert(i, lst.pop())
#             i = lst.index(x) // 2
# insert_x(200,lst)
# insert_x(10,lst)
# insert_x(50,lst)
# insert_x(5,lst)
# insert_x(5000,lst)
# insert_x(-1,lst)
#
# print(lst)


from random import randint

while True:
    print("Enter a number greater than or equal to 3 ")
    n = int(input())
    if n >= 3:
        break
    print("Try again ")
matrix = [[randint(1, 100) for j in range(n)] for i in range(n)]
ls = []
ls += (matrix[i][-i - 1] for i in range(len(matrix)))
print(min(ls))
