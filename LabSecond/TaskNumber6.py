# уникальные списки, т.е множества(sets)
first_set = set([1, 2, 3, 5])
second_set = set([1, 2, 5, 10, 16])

# симметричная разность аналогично отсутствию пересечения на диаграмме венна(Full Outer Join Excluding Inner Join в контексте SQL)
FullOuterJoinExcludingInnerJoin = first_set ^ second_set
print(FullOuterJoinExcludingInnerJoin)
