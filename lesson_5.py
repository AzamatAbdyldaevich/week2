# set
# seta = {"ss", (1,2,3,4,)}
#
# # frozenset
# frozen = frozenset(seta)
# frozen.update()
# print(type(frozen))

# def add(x, y):
#     return x + y
#
# print(add(2, 5))

# lists = [10000, 50000, 60000, 25000, 214521]
# dohod = sum(lists)
# procent = 0.2
# pribyl = dohod - dohod * procent
# # print(pribyl)
#
# def shop(lists, procent):
#     dohod = sum(lists)
#     prybl = dohod - dohod * procent
#     return prybl
#
# print(shop(lists, 0.1))

# def ploshad_pr(x, y):
#     s = x * y
#     return s
#
# print(ploshad_pr(5, 6))

list1 = [2, 3, 4, 5, 6]

# def factorial(l):
#     list2 = []
#     for i in l:
#         x = 1
#         for j in range(1, i + 1):
#             x *= j
#         list2.append(x)
#     return list2
#
#
# print(factorial(list1))

# 1
# a = int(input("Enter height:"))
# b = int(input("Enter width:"))
#
# def zvezda(x ,y):
#     for i in range(x):
#         zv = "*" * y
#         print(zv)

# zvezda(a, b)

# 2
# w = ["good", "great", "wow"]
#
#
# def voskl(www):
#     r = []
#     for i in w:
#         r.append(i + "!")
#     return r
#
#
# print(voskl(w))

# 3
l = [1, 6, 5, 11, 10]
n = int(input("Enter num:"))


def find_little_brother(l, n):
    min = 0
    for i in l:
        if i < n:
            if min < i:
                min = i
    return min


print(find_little_brother(l, n))
