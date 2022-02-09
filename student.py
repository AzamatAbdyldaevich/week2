john = [["algebra", 100], ["biologia", 84], ["fizika", 73], ["history", 61],
        ["english", 61], ["geograghi", 61], ["chemistry", 92]]
tom = [["algebra", 95], ["biologia", 88], ["fizika", 69], ["history", 70],
       ["english", 77], ["geograghi", 86], ["chemistry", 86]]
jim = [["algebra", 90], ["biologia", 83], ["fizika", 76], ["history", 81],
       ["english", 71], ["geograghi", 91], ["chemistry", 61]]

dict_john = dict(john)
ball_john = int(sum(dict_john.values()) / len(dict_john))

dict_tom = dict(tom)
ball_tom = int(sum(dict_tom.values()) / len(dict_tom))

dict_jim = dict(jim)
ball_jim = int(sum(dict_jim.values()) / len(dict_jim))

stud = {}
stud.setdefault("John", ball_john)
stud.setdefault("Tom", ball_tom)
stud.setdefault("Jim", ball_jim)
for i in stud:
    print("Средний балл", i, ":", stud.get(i), "баллов")
print("Лучшим студентом является:", max(stud, key=stud.get))