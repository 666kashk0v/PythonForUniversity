numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

minIndex = 0
#Find index which < minIndex. Update minIndex if i < minIndex
for i in range(0, len(numbers)):
    if numbers[i] < minIndex:
        minIndex = numbers[i]

print("Minimal index of array: ", numbers[minIndex])