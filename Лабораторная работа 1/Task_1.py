

class Cat:
    def __init__(self, color, age, weight):
        if age <= 0 or age > 30:
            raise ValueError("age must be greater than 0 and less than 30")
        if weight <= 0 or weight > 100:
            raise ValueError("weight must be greater than 0 and less than 100")
        self.color = color
        self.age = age
        self.weight = weight

    def meow(self):
        print("meow... meow... ")

    def eat(self, food_quantity_gr):
        if food_quantity_gr <= 0:
            raise ValueError("food quantity grams must be positive")
        elif food_quantity_gr > 1000:
            raise ValueError("BOOM!")
        elif food_quantity_gr > 200:
            self.weight += 0.0003 * food_quantity_gr
        print("miam... miam... ")


class Dog:
    def __init__(self, breed, sex, weight):
        if weight <= 0 or weight > 150:
            raise ValueError("weight must be greater than 0 and less than 150")
        if not (sex == "male" or sex == "female"):
            raise ValueError("sex must be male or female")
        self.sex = sex
        self.breed = breed
        self.weight = weight

    def bark(self):
        print("raaf... raaf... ")

    def run(self):
        self.weight -= 0.01


class PetHouse:
    def __init__(self, height, animal_type, color):
        if height <= 0:
            raise ValueError("height must be a positive number")
        self.height = height
        self.animal_type = animal_type
        self.color = color
        self.pet_inside = ""

    def enter(self, pet_name):
        self.pet_inside = pet_name

    def leave(self):
        self.pet_inside = ""


Akis = Cat("brown", 13, 4)
Paris = Cat("Black and White", 5, 8)
Jack = Dog("Labrador", "male", 20)
Tsiou = Dog("Pinscher", "male", 5)
ParisHouse = PetHouse(0.3, "cats house", "red")

Akis.meow()
Paris.eat(300)
print(Paris.weight)
Jack.run()
print(Jack.weight)
Tsiou.bark
ParisHouse.enter("Paris")
print(ParisHouse.pet_inside)
