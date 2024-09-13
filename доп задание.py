
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_ = sorted(list(students))

average_ = 0
i = 0
for i in range(len(grades)):
    average_ = [sum(grades[i]) / len(grades[i]) for i in range(len(grades))]
    break
slovar_2 = zip(students_, average_)
print(dict(list(slovar_2)))

