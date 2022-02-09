# dict - словари
# new_dict = {'x': 100, "y": 200
#             }
# new_dict1 = {
#     "Samat": {
#         "algebra":80,
#         "biology":90
#     },
# }
# print(new_dict1["Samat"]["biology"])
dicts = {
    "a": 4,
    "b": 5,
    "c": 7,
}
# for i, j in dicts.items():# values, keys
#     print(i, j)

# subject = {"algebra": 88,
#            "englih": 81,
#            "biology": 90
#            }
#
# s = 0
# for i in subject.values():
#     s += i
# print(s / len(subject))

# num = int(input("Enter num:"))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print("Fact = ", fact)

# new = dicts.fromkeys(["a", "b"])
# print(new)

# s = {1: 3, 4: 5}
# # print(s.get(8), 3)
# print(s.setdefault(5))
# print(s)

emp = {
    1: {
        "name": "Bek",
        "email": "bek@gmail.com",
        "age": "20",
        "salary": "1000"
    },
    2: {
        "name": "Aza",
        "email": "aza@gmail.com",
        "age": "30",
        "salary": "3000"

    },
    3: {
        "name": "Aida",
        "email": "aida@gmail.com",
        "age": "18",
        "salary": "1800"

    },
    4: {
        "name": "Sam",
        "email": "sam@gmail.com",
        "age": "22",
        "salary": "2200"
    },
    5: {
        "name": "Cris",
        "email": "cris@gmail.com",
        "age": "35",
        "salary": "3500"
    }
}
