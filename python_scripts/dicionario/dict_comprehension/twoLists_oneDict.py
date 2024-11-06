subjects = ["Math", "Portuguese", "English", "History"]
grade = [10, 8, 5, 3]

dicio = {subjects[i]: grade[i] for i in range(len(grade))}
dicio2 = {k:value for k, value in zip(subjects, grade)}

print(dicio)
print(dicio2)


