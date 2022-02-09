# s = input("Enter name:")
# d = ""
# f = 0
# # for i in range(len(s)):
# #     print(s[:i + 1]) # A Az Aza Azam...
# print("Vsego symbolov:", len(s))
# print("10 time:", s * 10)
# print("First symvol:", s[0])
# print("Last symvol:", s[-1])
# print("First 3 symvols:", s[:3])
# print("Last 3 symvols:", s[-3:])
# print("Back:", s[::-1])


# num = int(input("Enter num:"))
# for i in range(num):
#     print(" " * (i+1) + str(i+1))

# s = ["z", "m", "t"]
# l = "a".join(s)
# print(l)

# count articles with list comprehensions
s = input("Enter text:")
a = ["a", "an", "the"]
list_1 = s.split(" ")
# l = len[i for i in list_1 if i in a]
# print(len([i for i in list_1 if i in a]))
# list2 = [i for i in list_1[2::3]]
print([gebrai for i in list_1[2::3]])