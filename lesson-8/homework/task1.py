class Animal:
    def __init__(self, name, meal_type, use):
        self.name = name
        self.meal_type = meal_type
        self.use = use
    def __str__(self):
        return f"Animal(name:{self.name}, type of meal:{self.meal_type}, use:{self.use})"
    def carnivore(self):
        if self.meal_type == "meat":
            print("This animal is a carnivore")
        else:
            print("This animal is not a carnivore")
    def herbivore(self):
        if self.meal_type == "grass":
            print("This animal is a herbivore")
        else:
            print("This animal is not a herbivore")
class Cow(Animal):
    def __init__(self, name, meal_type, use, gender):
        super().__init__(name, meal_type, use)
        self.gender = gender
    def __str__(self):
        return f"Cow(name:{self.name}, type of meal:{self.meal_type}, use:{self.use}, gender:{self.gender})"
    def give_milk(self):
        if self.gender == "female":
            print("It gives milk")
        else:
            print("it doesn't")
class Fish(Animal):
    def __init__(self, name, meal_type, use, place):
        super().__init__(name, meal_type, use)
        self.place = place
    def __str__(self):
        return f"Fish(name:{self.name}, type of meal:{self.meal_type}, use:{self.use}, place of living:{self.place})"
    def guy(self):
        if self.name == " ":
            raise NameError("Name cannot be {self.name}")
        elif self.name == "Nemo":
            print("this guy likes cartoons")
        else:
            print("this guy hasn't watched the cartoon about nemo or doesn't like it")
class Sheep(Animal):
    def __init__(self, name, meal_type, use, place):
        super().__init__(name, meal_type, use)
        self.place = place
        self.sheep = []
    def __str__(self):
        return f"Sheep(name:{self.name}, type of meal:{self.meal_type}, use:{self.use}, place of living:{self.place})"
    def herd(self):
        sheep_count = len(self.sheep)
        if sheep_count == 0:
            return "there are no sheep in a herd"
        else:
            return f"there are {sheep_count} in a herd"
    def add(self, sheep):
        self.sheep.append(sheep)
        print("sheep is added successfully")
cow1 = Cow("yolanda", "grass", "for milk", "female")
cow1.give_milk()
fish1 = Fish("yolanda", " ", "meat", "water" )
fish1.guy()
