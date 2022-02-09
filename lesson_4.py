# # dict comprehention
#
# # dict_comp = {i: i**2 for i in range(1, 11)}
# # print(dict_comp)
#
# # dollars_2019 = {3: 209.7, 1: 69.7, 100: 6970, 8: 5000}
# # # dollar = 84.5
# # # dollars_2022 = {i:i * dollar for i in dollars_2019}
# # # print(dollars_2022)
# #
# # dict_num = {i: y for i, y in dollars_2019.items() if 5000 > y > 100}
# # print(dict_num)
#
# # lists = [1,1,4,3,6,8,6]
# # new_list = []
# # for i in lists:
# #     if lists.count(i) > 1:
# #         lists.remove(i)
# # print(lists)
#
# # lists = list(set(lists))
# # print(lists)
# # sets = {1,1,3,3,5,6,7}
# # set(pop)
# # set.remove(5)
# # print(sets)
# # print(dir(set))
# # set1 = {"a", "3"}
# # set2 = {2, 5, 7}
# # sets.update(set1)
# # # print(sets)
# #
# # a = sets.union(set2, set1)
# # print(a)
# # print(set1)
# # print(set2)
# # print(sets.isdisjoint(set1))
#
# # sets = {1,1,3,3,5,6,7}
# # set1 = {"a", "3"}
# # if sets.isdisjoint(set1):
# #     sets.update(set1)
# # print(sets)
#
# # sets = {1,1,3,3,5,6,7}
# # set2 = {"a", 7}
# # a = sets.difference(set2)
# # sets.symmetric_difference_update(set2)
# # print(a)
# # print(sets.symmetric_difference(set2))
# # print(sets.intersection(set2))
#
# stud = {
#     "Aza": 30,
#     "Bek": 20,
#     "Aida": 18,
#     "Nurgul": 25,
#     "Azim": 35,
#     "Tom": 20,
#     "Aika": 18,
#     "Mali": 25,
# }
# list_18 = []
# list_25 = []
# list_40 = []
# for i in stud.values():
#     if i <= 18:
#         list_18.append(i)
#     elif i <= 25:
#         list_25.append(i)
#     elif i > 25:
#         list_40.append(i)
#
# list_18 = list(set(list_18))
# list_25 = list(set(list_25))
# list_40 = list(set(list_40))
#
# print(list_18)
# print(list_25)
# print(list_40)

