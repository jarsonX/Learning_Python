----------------------------------------------------------------------------------------------THEORY
____________________________________________________________________________________________________

Object-oriented programming: #A programming paradigm where programmers define custom data types that 
#have custom methods embedded within them.

Object: #An object is a custom data structure that organizes and encapsulates variables and methods 
#into a single data type. It is used near-interchangeably with “instance.”

Class: #A custom data type comprised of multiple variables and/or methods. Instances or objects are 
#created based on the template provided by the class.

Instance: #A single set of values of a particular class. Classes may be comprised of multiple 
#variables; an instance is a set of values for these variables. The term “instance” is often used
#interchangeably with the term “object”.

Self: #Throughout nearly any Python code, self will be the keyword you see as the first parameter
#in every method in Python classes. However, technically you can use any other word if you want. 
#Python assigns the object containing the instance variables to the first parameter in the method, 
#no matter what it's called.
#Preceding any variable with self tells Python that the scope of such variable is the entire 
#lifespan of the class.
#Self is always the first parameter for any method defined inside of a class.

---------------------------------------------------------------------------------------------CLASSES
____________________________________________________________________________________________________
DEFINING

class Name:
  def __init__(self, firstname, lastname):               #__init__ is a constructor
    self.firstname = firstname                           #self.firstname is related to a class level
    self.lastname = lastname                             #firstname refers to a parameter
    
class Person:
  def __init__(self):
    self.name = Name()
    self.eycolor = 'brown'
    self.age = 30
    
a_name = Name('Jarson', 'X')    #Python automatically ignores the self parameter, goes to firstname    
a_person = Person()
a_person.age = 32               #accessing and modifying variables 
a_person.name.lastname = 'Y'

____________________________________________________________________________________________________
ENCAPSULATING METHODS IN CLASSES

Encapsulation: #The ability to combine variables and methods into class definitions in object-oriented
#programming. It helps avoid modification or misuse of data by other functions or programs.

Method: #A function defined inside of a class.
  
Scope: #The normal scope of a function, plus any variables that are visible in the instance of the 
#class as a whole.

#Four common method types are:

- Constructor: #specifies some code to run whenever a new instance of the class is created. Often has
      #parameters that provide values to the variables defined by the class.
      #Example: if class has a list, the list likely needs to be initialized before it can be used.
      #This would be done in the constructor.
- Destructor: #a special method called automatically during the destruction of an object.
      #Example: useful when dealing with massive quantities of data and running out of memory. Allows
      #to free up the memory by destroying instance that are no longer needed.
- Getter: #returns the value of variable contained within the class. Commonly used to allow other
      #processing to occur whenever the variable is accessed (like logging), which is usually not
      #possible when accessing variables directly (not through a method).
- Setter: #sets a variable contained within the class to a new value. Commonly used to allow other
      #processing to occur whenever the variable is changed (like logging).
     
