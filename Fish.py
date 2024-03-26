from Animal import Animal


class Fish(Animal):

    def __init__(self, name, age, gender, weight, species, fin_count, scale_color):
        super().__init__(name, age, gender, weight)
        self.__species = species
        self.__fin_count = fin_count
        self.__scale_color = scale_color

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def fin_count(self):
        return self.__fin_count

    @fin_count.setter
    def fin_count(self, fin_count):
        self.__fin_count = fin_count

    @property
    def scale_color(self):
        return self.__scale_color

    @scale_color.setter
    def scale_color(self, scale_color):
        self.__scale_color = scale_color

    def print_fish(self):
        self.print_animal()
        print(f'species: {self.species}, Fin count: {self.fin_count}, Scale color: {self.scale_color}')

    def make_sound(self):
        self.make_sound()
        print("Fish not making a sound")

    def move(self):
        print("the fish is swimming")
