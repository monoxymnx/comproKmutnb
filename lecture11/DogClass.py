class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def dedscription(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
mikey = Dog("Mikey", 6)
print(mikey.dedscription())
print(mikey.speak("Gruff gruff"))