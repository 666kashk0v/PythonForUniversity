#Create dictionary
students = {
    "Ivan": [9,9,7],
    "Andrew": [2,5,5],
    "Mikhail": [7,8,6]
}

#Add new key-value
students["Alex"] = [9,10,4]

#Delete by key
del students["Andrew"]

#Change value by key
students["Ivan"] = [2,2,2]

#Extract value by key
grade = students["Alex"]
print("Alex marks:", grade)

#Output finally dictionary
print("Updated dictionary info:", students)