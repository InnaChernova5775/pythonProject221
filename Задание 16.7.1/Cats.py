


class Cat:

    def __init__(self, name, gender, age):

        self.name = name
        self.gender = gender
        self.age = age

import json
with open('Cat list.json', encoding='utf8') as f:
    strFile=f.read()
    cats = json.loads(strFile)


print(cats)

for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age =cat.get("age"))

    print("Имя: ", cat_obj.name, " Пол: ", cat_obj.gender, " Возраст: ", cat_obj.age)








