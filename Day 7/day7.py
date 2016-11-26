#classes -> represents objects - duh!
class Animal:
    species="Carnivor"
    noise="Grunt"
    size="Big"
    age = 0
    def makeSound(self):
        return self.noise
    def mySize(self):
        return self.size
    def newAge(self,newAge):
        self.age = newAge
        return self.age

#Inheritance
#class -> kid class(Parent class)
class Dog(Animal):
    name = "Kiara"
    color="Trashy yellow"

myDoggo = Dog()
print(myDoggo.name)
print(myDoggo.color)
#receives from father
print(myDoggo.mySize())
print(myDoggo.makeSound())

#my new values
myDoggo.noise="Bark!"
myDoggo.size="Enormous!"
print(myDoggo.makeSound())
print(myDoggo.mySize())

#setting things via parameter
myDoggo.newAge(12)
print(myDoggo.age)
