# A My Family Trait Tree program that builds a parent class holding shared 
# family traits, a child class that inherits and adds its own details, overrides 
# a method to show everything together, and checks the family connection with 
# issubclass().
class Parent: 
    def __init__(self,eye_colour,hair,height):
        self.eye_colour=eye_colour
        self.hair=hair
        self.height=height
    def display(self):
        print(self.eye_colour)
        print(self.hair)
        print(self.height)
class Child(Parent):
    def __init__ (self,eye_colour,hair,height,name):
        self.name=name
        Parent.__init__(self,eye_colour,hair,height)
c=Child("black","brown","5'2","Bob")
c.display()