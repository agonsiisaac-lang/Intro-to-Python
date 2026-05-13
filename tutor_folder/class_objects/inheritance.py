"""inheritance allows a new class (child class) to inherit properties 
and behaviors from an existing class (parent class)."""

class Animal:
    def sound(self):
        return "Some sound"
    
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!


"""Method overriding allows a child class to provide a specific implementation 
of a method that is already defined in its parent class."""

class Vehicle:
    def move(self):
        return "The vehicle is moving"
    
class Car(Vehicle):
    def move(self):
        return "The car is driving"
class Bike(Vehicle):
    def move(self):
        return "The bike is pedaling"
    
car = Car()
bike = Bike()

print(car.move())  # Output: The car is driving
print(bike.move())  # Output: The bike is pedaling


"""
Explanation of everything in steps 
1. We define a parent class called `Animal` with a method `sound()` that returns a generic sound.
2. We create two child classes, `Dog` and `Cat`, that inherit from the `Animal` class. Each child class overrides the `sound()` method to return a specific sound for that animal.
3. We create instances of the `Dog` and `Cat` classes and call their `sound()` methods to see the overridden behavior.
4. We define another parent class called `Vehicle` with a method `move()` that returns a generic movement description.
5. We create two child classes, `Car` and `Bike`, that inherit from the `Vehicle` class. Each child class overrides the `move()` method to return a specific movement description for that type of vehicle.
6. We create instances of the `Car` and `Bike` classes and call their `move()` methods to see the overridden behavior.
7. This demonstrates how inheritance allows us to create new classes that reuse and extend the functionality of"""