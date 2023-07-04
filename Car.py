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

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

# Create a Car object
car = Car(2022, "Tesla")

# Accelerate and display current speed
print("Accelerating:")
for _ in range(5):
    car.accelerate()
    print("Current speed:", car.get_speed())

# Brake and display current speed
print("Braking:")
for _ in range(5):
    car.brake()
    print("Current speed:", car.get_speed())
