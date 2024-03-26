class Animal:
    def __init__(self, name, age, gender, weight):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def print_animal(self):
        print(f'Name: {self.name}, Age: {self.age}, Gender: {self.gender},Weight: {self.weight}')

    def make_sound(self):
        print('weeeeee')

    def move(self):
        print('Im moving')
