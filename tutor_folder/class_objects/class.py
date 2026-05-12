# class OOP

class Car:
    pass

my_car = Car()

#print(my_car)

class Car:
    brand = "Toyota"
    model = "Camry"

car1 = Car()
#print(car1.brand)
#print(car1.model)
#print(car1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

p1 = Person("Alice", 30)
print(p1.name)  
print(p1.age)
print(p1)