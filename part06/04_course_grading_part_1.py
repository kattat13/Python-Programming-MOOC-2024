if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"


names = {}

with open(student_info) as file:
    for line in file:
        items = line.split(';')
        if items[0] == 'id':
            continue
        names[items[0]] = items[1:]

exercises = {}

with open(exercise_data) as file:
    for line in file:
        items = line.split(';')
        if items[0] == 'id':
            continue
        exercises[items[0]] = items[1:]

for idx, name in names.items():
    print(' '.join(name).strip(), sum(int(x) for x in exercises[idx]))