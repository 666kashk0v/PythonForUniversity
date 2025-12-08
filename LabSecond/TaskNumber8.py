def find_average(numbers):
    return sum(numbers) / len(numbers)

def update_list(numbers, average):

    #new_numbers = []
    #for number in numbers:
    #    if number > average:
    #        new_numbers.append(number)
    #return new_numbers


    # удалять данные плохая практика, поэтому способ с сохранением первичного списка написан выше
    i = 0
    while i < len(numbers):
        if numbers[i] < average:
            numbers.pop(i)  # удаляем по индексу
        else:
            i += 1
    return numbers


numbers = [1, 2, 5, 10, 16]

average = (find_average(numbers))
print("Average of list", average)

print("Updated list:",update_list(numbers, average))