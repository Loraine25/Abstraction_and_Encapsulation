# Abstraction_and_Encapsulation

The concepts of abstraction and encapsulation in this application are shown using the Python programming language. In addition, it contains three (3) different classifications, including Fan, Car, and Pet. These three (3) classifications each have unique purposes that will be discussed below.

# FAN CLASS

A fan class that represents an electric fan is created with this code. It offers techniques for locating and setting up different fan settings including speed, status, radius, and color.

- The fan's slow speed is represented by the parameter SLOW, which has a value of 1.
- The fan's middle speed is represented by the parameter middle, which has a value of 2.
- The fan's fast speed is represented by the parameter FAST, which has a value of 3.
- Sets the fan's starting speed with speed (default: SLOW).
- Determines whether the fan is turned on (True) or off (False) upon startup.
- radius (default: 5): Sets the radius of the fan.
- color: Indicates the color of the fan (by default, "blue").

# CAR CLASS 

This class simulates an automobile; like a real car, it has the ability to brake, accelerate, change speed, and be controlled. It also shows your current speed. Users can also interact with characteristics like model year, brand, and speed.
A new vehicle object with the specified year, model, and make is created by the function

-__init__(self, yearmodel, make).
- Using the function accelerate(self), you can make the automobile go five miles per hour faster.
- brake(self): This feature aids in a 5-mph speed reduction for the vehicle.
- The speed of the vehicle is returned by get_speed(self).

# PET CLASS 

This code describes Pet, a simple application that lets users enter information about their pets and shows the name, breed, and age of the animal. 

- By calling this method with the default parameters for name, animal type, and age, a new pet object is created.
- The function set_name(self, name) changes the pet's name.
- The function set_animal_type(self, animal_type) changes the pet's animal type.
- The age of the pet is set using set_age(self, age).
