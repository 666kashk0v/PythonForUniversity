#Try-catch for ValueType error
while True:
    try:
        print("Enter integer value: ")
        n = int(input())
        break
    except ValueError:
        print("Your entered non integer value")

#Create list of dividers
dividers = []

#Find dividers and add it in list
for i in range(1, n + 1):
    if n % i == 0:
        dividers.append(i)

#Show dividers of entered value
print("The list of dividers: ", dividers)

#Show count of dividers
print("The count of dividers: ", len(dividers))