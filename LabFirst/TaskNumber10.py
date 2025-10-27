import math # Library for trigonometry

print("Enter α value(in °): ")
a = math.radians(float(input())) # /math.radians because function take PI value

print("Enter φ value(in °): ")
phi = math.radians(float(input())) # /math.radians because function take PI value

# Calculate result for z1 expression
def CalculateZ1(a, phi):
    numeratorZ1 = 1 / (math.sin(3 * a) ** 2) + math.cos(7 * a) - math.sin(6 * a)
    denominatorZ1 = math.tan(a) + phi - 2 * a
    if denominatorZ1 == 0:
        print("Error: denominator = 0")
        return None # Bad exception
    resultZ1 = numeratorZ1 / denominatorZ1
    return resultZ1

# Calculate result for z2 expression
def CalculateZ2(a):
    resultZ2 = 13 * (math.tan(a) ** 2) - 54 * math.tan(a) + 98
    return resultZ2

# Functions call
print("Z1 result: ", CalculateZ1(a, phi))
print("Z2 result: ", CalculateZ2(a))