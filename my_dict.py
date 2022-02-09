my_dict = {
    'a': 500,
    'b': 5874,
    'c': 560,
    'd': 400,
    'e': 5874,
    'f': 20,
}
max_keys = []   # список ключей у которых значения максимальные
counter = 0
while counter < 3:
    max_value = max(my_dict.values())
    for i in my_dict.keys():
        if my_dict.get(i) == max_value:
            max_keys.append(i)
            my_dict.pop(i)
            counter += 1
            break

print(my_dict)
print(max_keys)