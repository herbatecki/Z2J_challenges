class Animal():

  def __init__(self, age, sex, name):
    self.age = age
    self.sex = sex
    self.name = name

  def __str__(self):
    return f"Our animal on the farm is {self.name}, {self.age} years old and it is {self.sex}."

  def speak(self, sound):
    return f"{self.name} makes a noise called: {sound}."

class Poultry(Animal):

  legs = "claw"
  upper_limbs = "wings"


class Chicken(Poultry):
  
  def speak(self, sound="cackling"):
    return super().speak(sound)

class Duck(Poultry):

  def speak(self, sound="quacking"):
    return super().speak(sound)
  
class Goose(Poultry):

  def speak(self, sound="honking"):
    return super().speak(sound)

class Bovidae(Animal):

 legs = "foot"

class Cow(Bovidae):

  def speak(self, sound="mooing"):
    return super().speak(sound)

class Goat(Bovidae):

  def speak(self, sound="bleating"):
    return super().speak(sound)

class Sheep(Bovidae):
  
  def speak(self, sound="bleating"):
    return super().speak(sound)

class Pig(Animal):
  legs = "hoof"

  def speak(self, sound='squealing'):
    return super().speak(sound)
  


peppa = Pig(8, "female","Peppa")
print(peppa)
print(peppa.speak())
print(peppa.legs)
print()
koko = Chicken(2, "male", "Koko")
print(koko.legs)
print(koko.upper_limbs)
print(koko)
print(koko.speak())

  

  
  
