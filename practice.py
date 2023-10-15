# i = 1
# while (i<5):
#     pass

# for j in range(5):
#     pass

# if (i == 2):
#     pass
# list =[1,2,3,4,5,6,]
# print(sum(list))

# from functools import reduce
# square = lambda x : x*x
# l = [2,3,4,5,6,7,8,9,8,9,0]
# newl = list(map(square,l))
# print(newl)
# newl1 = list(filter(lambda a : a>3,l))
# print(newl1)
# l1 = [2,2,2,2,2,2,2,2,2,2]
# newl2 = reduce(lambda a,b: (a*b),l1)
# print(newl2)
# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())