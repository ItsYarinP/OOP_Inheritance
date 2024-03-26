from Animal import Animal


class Dog(Animal):

    def __init__(self, name, age, gender, weight, breed, tail_length, bark_volume):
        super().__init__(name, age, gender, weight)
        self.__breed = breed
        self.__tail_length = tail_length
        self.__bark_volume = bark_volume

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @property
    def tail_length(self):
        return self.__tail_length

    @tail_length.setter
    def tail_length(self, tail_length):
        self.__tail_length = tail_length

    @property
    def bark_volume(self):
        return self.__bark_volume

    @bark_volume.setter
    def bark_volume(self, bark_volume):
        self.__bark_volume = bark_volume

    def print_dog(self):
        self.print_animal()
        print(f'Breed: {self.breed}, Tail length: {self.tail_length}, Bark volume: {self.bark_volume}')

    def make_sound(self):
        print("Woof!")

    def move(self):
        print("the dog is running")
