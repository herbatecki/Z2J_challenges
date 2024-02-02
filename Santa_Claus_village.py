class Boss_Santa():

  def __init__(self, name, age, clothes, characteristic_sign, function):
    self.name = name
    self.age = age
    self.clothes = clothes
    self.characteristic_sign = characteristic_sign
    self.function = function

  def __str__(self):
    return f"{self.name} is {self.age} years old, has {self.clothes} clothes, his attribute is {self.characteristic_sign} and he is {self.function} in the village."

  def reading_lists(self, childrens_lists):
    return f"{self.name} can read all of {childrens_lists}."

  def providing_presents(self, means_of_transport):
    return f"{self.name} provide presents by {means_of_transport}."


class Santa_elf(Boss_Santa):

  def assigning_tasks(self, activity):
    return f"{self.name} can {activity} tasks in factory of presents."

  def reading_lists(self, childrens_lists="childrens lists submitted by Santa Claus"):
    return super().reading_lists(childrens_lists)


class Santa_gnome(Santa_elf):

  def producing_presents(self):
    return f"{self.name} can produce presents in factory of presents"

  def assigning_tasks(self, activity="realize"):
    return super().assigning_tasks(activity)


santa = Boss_Santa("Niclaus", 150, "red-white", "bag of presents", "boss")
print(santa)
print(santa.reading_lists("childrens list"))
merry = Santa_elf("Merry", 120, "green-red", "pointed ears", "supporter")
print(merry)
print(merry.assigning_tasks("distribute"))
goblin = Santa_gnome("Goblin", 135, "grey", "big cap", "worker")
print(goblin)
print(goblin.assigning_tasks())
