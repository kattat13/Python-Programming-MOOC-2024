def add_student(database: dict, name: str):
    database[name] = {}


def add_course(database: dict, name: str, course: tuple):
    # ignore courses with grade 0
    if course[1] == 0:
        return
    # check if course is repeated
    elif course[0] in database[name]:
        if database[name][course[0]] < course[1]:
            database[name][course[0]] = course[1]
    # new course
    else: 
        new_dict = {}
        new_dict[course[0]] = course[1]
        database[name].update(new_dict)


def calc_avg_grade(grades: list) -> float:
    return sum(grades) / len(grades)


def print_student(database: dict, name: str):
    if name in database:
        print(f'{name}:')
        if database[name]:
            grades = []
            print(f' {len(database[name])} completed courses:')
            for key, value in database[name].items():
                print(f'  {key} {value}')
                grades.append(value)
            print(f' average grade {calc_avg_grade(grades)}')
        else:             
            print(f' no completed courses')
    else:
            print(f'{name}: no such person in the database')


def summary(database: dict):
    most_courses = 0
    most_courses_name = ''
    best_avg = 0
    best_avg_name = ''
    for student, courses_data in database.items():
        if len(courses_data) > most_courses:
            most_courses = len(courses_data)
            most_courses_name = student
        avg_grade = calc_avg_grade(courses_data.values())
        if avg_grade > best_avg:
            best_avg = avg_grade
            best_avg_name = student
            
    print(f'students {len(database)}')
    print(f'most courses completed {most_courses} {most_courses_name}')
    print(f'best average grade {best_avg} {best_avg_name}')
    

if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)