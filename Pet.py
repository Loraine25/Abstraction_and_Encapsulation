# Anonuevo, Loraine N.
# BSCPE 1-4

# Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mHi! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

# Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mLoraine\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm glad that you're here!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, sit back and learn with me!\033[0m")

class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Create a Pet object
pet = Pet()

# Prompt the user to enter pet's details
name = input("Enter pet's name: ")
animal_type = input("Enter pet's animal type: ")
age = input("Enter pet's age: ")

# Set the pet's attributes
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

# Display pet's details
print("Pet's details:")
print("Name:", pet.get_name())
print("Animal type:", pet.get_animal_type())
print("Age:", pet.get_age())
