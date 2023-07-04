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

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

# Constructor 
    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        # Private int data field named speed that specifies the speed of the fan.
        self.__speed = int(speed)
        # Private bool data field named on that specifies whether the fan is on.
        self.__on = bool(on)
        # Private float data field named radius that specifies the radius of the fan.
        self.__radius = float(radius)
        # Private string data field named color that specifies the color of the fan.
        self.__color = str(color)

# Getter methods for all four data fields.
    def get_speed(self):
        # Get the fan speed.
        return self.__speed
    
    def is_on(self):
        # Check if the fan is on.
        return self.__on
    
    def get_radius(self):
        # Get the radius of the fan.
        return self.__radius
    
    def get_color(self):
        # Get the color of the fan.
        return self.__color
    
    # Setter methods for all four data fields.
    def set_speed(self, speed):
        # Set the fan speed.
        self.__speed = int(speed)

    def set_on(self, on):
        # Set whether the fan is on or off.
        self.__on = bool(on)

    def set_radius(self, radius):
        # Set the radius of the fan.
        self.__radius = float(radius)

    def set_color(self, color):
        # Set the color of the fan.
        self.__color = str(color)

class Fan:
    # Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3.
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        # Private int data field named speed that specifies the speed of the fan.
        self.__speed = int(speed)
        # Private bool data field named on that specifies whether the fan is on.
        self.__on = bool(on)
        # Private float data field named radius that specifies the radius of the fan.
        self.__radius = float(radius)
        # Private string data field named color that specifies the color of the fan.
        self.__color = str(color)

    # Getter methods for all four data fields.
    def get_speed(self):
        # Get the fan speed.
        return self.__speed
    
    def is_on(self):
        # Check if the fan is on.
        return self.__on
    
    def get_radius(self):
        # Get the radius of the fan.
        return self.__radius
    
    def get_color(self):
        # Get the color of the fan.
        return self.__color
    
    # Setter methods for all four data fields.
    def set_speed(self, speed):
        # Set the fan speed.
        self.__speed = int(speed)

    def set_on(self, on):
        # Set whether the fan is on or off.
        self.__on = bool(on)

    def set_radius(self, radius):
        # Set the radius of the fan.
        self.__radius = float(radius)

    def set_color(self, color):
        # Set the color of the fan.
        self.__color = str(color)


class TestFan:
    def __init__(self):
        fan1 = Fan(Fan.FAST, True, 10, "yellow")
        fan2 = Fan(Fan.MEDIUM, False, 5, "blue")

        self.display_fan_properties(fan1)
        self.display_fan_properties(fan2)

    def display_fan_properties(self, fan):
        print("Fan Speed:", fan.get_speed())
        print("Fan On:", fan.is_on())
        print("Fan Radius:", fan.get_radius())
        print("Fan Color:", fan.get_color())
        print()


# Create an instance of the TestFan class to run the test program
TestFan()
