from Animal import Animal


class Bird(Animal):

    def __init__(self, name, age, gender, weight, species, wing_span, beak_length):
        super().__init__(name, age, gender, weight)
        self.__species = species
        self.__wing_span = wing_span
        self.__beak_length = beak_length

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def wing_span(self):
        return self.__wing_span

    @wing_span.setter
    def wing_span(self, wing_span):
        self.__wing_span = wing_span

    @property
    def beak_length(self):
        return self.__beak_length

    @beak_length.setter
    def beak_length(self, beak_length):
        self.__beak_length = beak_length

    def print_bird(self):
        self.print_animal()
        print(f'species: {self.species}, Wing span: {self.wing_span}, Beak length: {self.beak_length}')

    def make_sound(self):
        print("Chirp chirp!")

    def move(self):
        print("the bird is flying")
