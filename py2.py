class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2020 - self.year


MyCar = Car(1999, "ford", "truck")
print(MyCar.age())


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana" & "cherry":
        break


for x in range(00):
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for Z in fruits:
        print(x, z)
