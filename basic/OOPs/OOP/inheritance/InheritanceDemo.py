# parent class
class Parent:

   def __init__(self, name, age, salary):
      self.name = name  # public variable
      self.__age = age  # private variable
      self._salary = salary  # protected variable

   def parentMethod(self):
      print ("Calling parent method")

# child class
class Child(Parent):

   def childMethod(self):
      print ("Calling child method" + self._salary)

# instance of child
c = Child()  
# calling method of child class
c.childMethod() 
# calling method of parent class
c.parentMethod()