#Create tuple
arbitraryTuple=(52,"HelloWorld", [1,2,3], 3.14)

#Try to change the tuple
try:
    arbitraryTuple[0] = 228
except TypeError: #Catch error
    print("Does not support item assignment")

#Extract element by index
print(arbitraryTuple[1])