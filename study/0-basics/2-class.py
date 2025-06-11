# Class
class Animal:

  # Props
  name="Parinda"

  # Method
  def fly(self):
    print("I can fly " + self.name)


# object variable
a1 = Animal()
a2 = Animal()

a1.name = "Badal Dia"


print(a1.name)
print(a2.name)

a1.fly()


print(Animal().name)