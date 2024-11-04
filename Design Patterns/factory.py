# Product Interface
class Animal:
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory Class
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

# Test the Factory Pattern
if __name__ == "__main__":
    animal = AnimalFactory.get_animal("dog")
    print(animal.speak())  # Output: Woof!
    print(type(animal))

    animal = AnimalFactory.get_animal("cat")
    print(animal.speak())  # Output: Meow!
    print(type(animal))