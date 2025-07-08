"""
The Factory pattern provides an interface for creating objects in a
superclass but allows subclasses to alter the type of objects that will be created.

"""

class AnimalFactory:
    @staticmethod
    def get_animal(type_):
        if type_ == "dog":
            return Dog()
        elif type_ == "cat":
            return Cat()
        else:
            return None

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Usage
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Woof!


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


class Square(Shape):
    def draw(self):
        print("Drawing a Square")


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")