from random import randint
secret_num = randint(1, 100)
num = 0
bolshe = 1
menshe = 100
for i in range(5):
    num = int(input("Введите число:"))
    if secret_num < num:
        menshe = num
        print("Меньше, осталось", 4 - i, "ввода, введите число между", bolshe, "и", menshe, ":")
    elif secret_num > num:
        bolshe = num
        print("Больше, осталось", 4 - i, "ввода, введите число между", bolshe, "и", menshe), ":"
    else:
        print("Урраа, Вы угадали !!!")
        break
else:
    print("Вы проиграли, загаданное число было:", secret_num)