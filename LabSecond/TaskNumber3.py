#key = string; value = len(string)
new_dictionary = {
    "London" : 6,
    "Britain" : 7
}

#Enter string
print("Enter string: ")
new_string = str(input())

#Add new element of dictionary
new_dictionary[new_string] = len(new_string)
print(new_dictionary)

#Delete element from dictionary
del new_dictionary["London"]