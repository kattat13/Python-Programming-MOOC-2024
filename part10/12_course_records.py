
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.name = name
        self.grade = grade
        self.credits = credits


class Records:
    def __init__(self):
        self.courses = []

    def add_course(self, name: str, grade: int, credits: int):
        for course in self.courses:
            if course.name == name:
                if course.grade < grade:
                    course.grade = grade
                    return
                return
        else:
            self.courses.append(Course(name, grade, credits))

    def get_course_data(self, name: str):
        for course in self.courses:
            if course.name == name:
                print(f'{course.name} ({course.credits} cr) grade {course.grade}')
                return
        print('no entry for this course')

    def statistics(self):
        grades = {
            1: 0, 
            2: 0,
            3: 0,
            4: 0,
            5: 0
            }
        completed = len(self.courses)
        credits_sum = 0
        grades_sum = 0
        for course in self.courses:
            credits_sum += course.credits
            grades[course.grade] += 1
            grades_sum += course.grade
        print(f'{completed} completed courses, a total of {credits_sum} credits')
        print('grade distribution')
        print(f'mean {grades_sum / completed:.1f}')
        for k, v in grades.items():
            print(f'{k}: {"x"*v}')



class CourseApp:
    def __init__(self):
        self.course_records = Records()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

    def add_course(self):
        name = input('course: ')
        grade = int(input('grade: '))
        credits = int(input('credits: '))
        self.course_records.add_course(name, grade, credits)

    def get_course_data(self):
        name = input('course: ')
        self.course_records.get_course_data(name)

    def statistics(self):
        self.course_records.statistics()


application = CourseApp()
application.execute()