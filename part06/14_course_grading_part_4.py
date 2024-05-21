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
    student_info = input('Student information: ')
    exercise_data = input('Exercises completed: ')
    exam_points = input('Exam points: ')
    course_info = input('Course information: ')
else:
    # hard-coded input
    student_info = 'students1.csv'
    exercise_data = 'exercises1.csv'
    exam_points = 'exam_points1.csv'
    course_info = 'course1.txt'


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


# read course information
# retrieve course name and study credits
course_f = open(course_info).read()
course_name = course_f.split('\n')[0].split(':')[1].strip()
course_credits = course_f.split('\n')[1].split(':')[1].strip()

# statistics in columns
columns = ['name', '', '', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade']

columns_line = ''
for element in columns:
    columns_line += f'{element:10}'


# create results.txt file
with open('results.txt', 'w') as r_file, open('results.csv', 'w') as r_csv:
    # write headers to results.txt
    r_file.write(f'{course_name}, {course_credits} credits\n')
    r_file.write(f"{'=' * 38}\n")
    r_file.write(f'{columns_line}\n')
    # write statistics
    for idx, name in names.items():
        exercises_graded = grade_excercises(exercises[idx])
        grade = final_grade(exercises_graded + exams[idx])
        line = ''
        line += f'{name:30}'
        line += f'{exercises[idx]:<10}'
        line += f'{exercises_graded:<10}'
        line += f'{exams[idx]:<10}'
        line += f'{exercises_graded + exams[idx]:<10}'
        line += f'{grade:<10}'
        r_file.write(f'{line}\n')
        r_csv.write(f'{idx};{name};{grade}\n')
        
