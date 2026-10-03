class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

a=Animal()
d=Dog()
c=Cat()

a.eat()
d.sound()
c.sound()
