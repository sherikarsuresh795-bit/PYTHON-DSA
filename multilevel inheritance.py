class animal:
    def eat(self):
        print("animal eat")
class mammal(animal):
    def walk(self):
        print("mammal walk")
class dog(mammal):
    def speak(self):
        print("dog bark")
o=dog()
o.eat()
o.speak()
o.walk()