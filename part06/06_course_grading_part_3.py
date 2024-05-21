def grade_excercises(points):
    return int(points / 40 * 10)


def final_grade(points):
    if points >= 28:
        return 5
    elif points >= 24:
        return 4
    elif points >= 21:
        return 3
    elif points >= 18:
        return 2
    elif points >= 15:
        return 1
    else:
        return 0


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


# statistics in columns
columns = ['name', '', '', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade']

for element in columns:
    print(f'{element:10}', end='')
print()

for idx, name in names.items():
    exercises_graded = grade_excercises(exercises[idx])
    print(f'{name:30}', end='')
    print(f'{exercises[idx]:<10}', end='')
    print(f'{exercises_graded:<10}', end='')
    print(f'{exams[idx]:<10}', end='')
    print(f'{exercises_graded + exams[idx]:<10}', end='')
    print(f'{final_grade(exercises_graded + exams[idx]):<10}')
    



