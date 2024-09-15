grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_sr = []
for i in grades:
    s = sum(i)/len(i)
    grades_sr.append(s)
#print(grades_sr)
students_ab = sorted(students)
#print(students_ab)
dict_ = dict(zip(students_ab, grades_sr))
print(dict_)

