text = '''В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера».
Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты, 
где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности.
В 1965 году результат был уже лучше — 24 000 км.
Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении, 
что использовали при построении следующих аппаратов.
Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году.
А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.
'''
# удаляем лишние символы
text = text.replace("-", " ")
text = text.replace("\n", "")
text = text.replace(".", " ")
text = text.replace(",", "")
text = text.replace("«", "")
text = text.replace("»", "")

# создаем список слов через пробелы
list1 = text.split(" ")
# 1. Наиболее часто встречающееся слово:
# из листа формируем словарь: {ключ: слово, значение: кол-во этого слова в тексте}
dict1 = {i: list1.count(i) for i in list1 if len(i) > 1}    # не учитывая предлоги

# выводим ключ с максимальным значением кол-ва слова
print("Самое частое встречающееся слово -", max(dict1, key=dict1.get))

# 2. Cамое длинное слово:
# из листа формируем словарь: {ключ: слово, значение: кол-во символов слова}
dict2 = {i: len(i) for i in list1}

# выводим ключ с максимальным значением кол-ва символов
print("Самое длинное слово -", max(dict2, key=dict2.get))