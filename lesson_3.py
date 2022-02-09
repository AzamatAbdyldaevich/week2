# list comprehentions
# генераторы списков

# list_a = []
# for i in range(1, 101):
#     list_a.append(i)
# print(list_a)
# list_num = [1024, 4, 36, 200, 90]
# list_b = [i for i in range(1, 101) if i in list_num]
# print(list_b)

# string_list = ["banana", "apanas", "apple", "oranle"]
# # new_str = [i for i in string_list if i[-2] == "l"]
# ap_list = [i for i in string_list if i.startswith("ap")]
# print(ap_list)

# from datetime import datetime
# before = datetime.now()
# list1 = []
# for i in range(1, 10000):
#     list1.append(i)
# after = datetime.now() - before
# print(after)
# b = datetime.now()
# list_comp = [i for i in range(1, 10000)]
# print(datetime.now() - b)

# list1 = ["+996555905136","+99670005136","+996556557783","+996777905136","+996772617503", "+996705556677"]
# mega_list = [("Я использую Мегаком с номером" + i) for i in list1 if i.startswith("+99655")]
# bee_list = [("Я использую Beeline с номером" + i) for i in list1 if i.startswith("+99677")]
# o_list = [("Я использую Nur с номером" + i) for i in list1 if i.startswith("+99670")]
# print(mega_list)
# print(bee_list)
# print(o_list)

# pr = {}
# for i in range(5):
#     product = input("Enter product:")
#     price = input("Enter price:")
#     pr.setdefault(product, price)
#
# for i in pr.keys():
#     pr[i] += "$"
# print(pr)

users = {
    "Tom": "123",
    "Sam": "456",
    "Ted": "777",
    "Aza": "888",
    "Tod": "666",
}
wrong_pass = 0
user_name = input("Enter user name:")
user_pass = input("Enter password:")

for i in users:
    if i == user_name and users.get(i) == user_pass:
        print("You can enter!")
        wrong_pass = -1
        break
    elif i == user_name and users.get(i) != user_pass:
        wrong_pass = 1

if wrong_pass == 1:
    print("Wrong password!")
elif wrong_pass == 0:
    print("Not found user!")
