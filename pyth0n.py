name = "Kim"
age = 44
sentence = f"Hi my name is {name} and I am {44} years old!"
print(sentence)
# //////////////////////////////////
Birthyear = 1900
if 2000 <= Birthyear < 2100:
    print("Welcome to the 21st century")
else:
    print("Your born before the 21st")
# /////////////////////////////////////


def triplePrint(word):
    print(word*3)


triplePrint("Trees ")
# /////////////////////////////////////
# LIST(arrays)
shoes = ["Nike", "Under Armour", "Puma", "K-Swiss"]
print(shoes)

# /////////////////////////////////////
# LOOPS
numbers = [4, 24, 50, 59, 71, 8, 74, 44, 92, 1000, 90]
for num in numbers:
    if num >= 90:
        print(num)
# /////////////////////////////////////
words = ["Summer", "Sale", "Save Big"]
definitions = ["1 of 4 Seasons",
               "exchange of a commodity for money", "common term used in sales"]

homemadeDictionary = {}
for i in range(0, 3):
    homemadeDictionary[words[i]] = definitions[i]
print(homemadeDictionary)
# /////////////////////////////////////
# CLASSES


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2020 - self.year


age()


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("ROAR BARK!")


myDog = Dog("Fred", "blue")

print(myDog.color)
