def grade_excercises(points):
    return int(points / 40 * 10)


if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = 'exam_points1.csv'


names = {}

with open(student_info) as file:
    for line in file:
        items = line.split(';')
        if items[0] == 'id':
            continue
        names[items[0]] = ' '.join(items[1:]).strip()

exercises = {}

with open(exercise_data) as file:
    for line in file:
        items = line.split(';')
        if items[0] == 'id':
            continue
        exercises[items[0]] = sum(int(x) for x in items[1:])

exams = {}

with open(exam_points) as file:
    for line in file:
        items = line.split(';')
        if items[0] == 'id':
            continue
        exams[items[0]] = sum(int(x) for x in items[1:])


for idx, name in names.items():
    print(name, end=' ')

    grade = grade_excercises(exercises[idx]) + exams[idx]
    if grade >= 28:
        print(5)
    elif grade >= 24:
        print(4)
    elif grade >= 21:
        print(3)
    elif grade >= 18:
        print(2)
    elif grade >= 15:
        print(1)
    else:
        print(0)




