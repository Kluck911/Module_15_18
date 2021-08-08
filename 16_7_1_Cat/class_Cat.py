class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getDescription(self):
        print(f'Кличка: {self.getName()}')
        print(f'Пол: {self.getSex()}')
        print(f'Возраст: {self.getAge()}')
        return
