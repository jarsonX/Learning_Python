----------------------------------------------------------------------------------------------THEORY
____________________________________________________________________________________________________

Object-oriented programming: A programming paradigm where programmers define custom data types that 
have custom methods embedded within them.

Object: An object is a custom data structure that organizes and encapsulates variables and methods 
into a single data type. It is used near-interchangeably with “instance.”

Class: A custom data type comprised of multiple variables and/or methods. Instances or objects are 
created based on the template provided by the class.

Instance: A single set of values of a particular class. Classes may be comprised of multiple 
variables; an instance is a set of values for these variables. The term “instance” is often used
interchangeably with the term “object”.

Self: Throughout nearly any Python code, self will be the keyword you see as the first parameter
in every method in Python classes. However, technically you can use any other word if you want. 
Python assigns the object containing the instance variables to the first parameter in the method, 
no matter what it's called.


------------------------------------------------------------------------------------DEFINING-CLASSES
____________________________________________________________________________________________________

class Name:
  def __init__(self):
    self.firstname = 'Jarson'
    self.lastname = 'X'
    
class Person:
  def __init__(self):
    self.name = Name()
    self.eycolor = 'brown'
    self.age = 30
    
a_person = Person()
a_person.age = 32               #accessing and modifying variables 
a_person.name.lastname = 'Y'
