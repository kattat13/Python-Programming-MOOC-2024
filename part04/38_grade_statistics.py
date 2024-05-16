def inputs_from_user():
    all_inputs = []
    real_scores = []

    while True:
        user = input('Exam points and exercises completed: ')
        if user == '':
            break
        exam_points, excersise_points = user.split(' ')
        total_points = calculate_exam_points(exam_points, excersise_points)
        all_inputs.append(total_points)
        real_scores.append(total_points)
        if int(exam_points) < 10:
            real_scores[-1] = 0
        
    return all_inputs, real_scores


def calculate_exam_points(exam_points: int, excersise_points: str):
    total_points = int(exam_points) + int(excersise_points) // 10
    return total_points


def calculate_average(total_points: list):
    return sum(total_points) / len(total_points)


def pass_percentage(failed: int, students: int):
    return round((1.0 - failed / students) * 100, 1)


def grades(real_scores):
    star = '*'
    grade_1 = 0
    grade_2 = 0
    grade_3 = 0
    grade_4 = 0
    grade_5 = 0
    fail = 0
    for points in real_scores:
        if points >= 28:
            grade_5 += 1
        elif points >= 24:
            grade_4 += 1
        elif points >= 21:
            grade_3 += 1
        elif points >= 18:
            grade_2 += 1
        elif points >= 15:
            grade_1 += 1
        else:
            fail += 1
    grade_dist = f'Grade distribution:\n  5: {star * grade_5}\n  4: {star * grade_4}\n  3: {star * grade_3}\n  2: {star * grade_2}\n  1: {star * grade_1}\n  0: {star * fail}\n'
    return grade_dist, fail







all_inputs, real_scores = inputs_from_user()
average = calculate_average(all_inputs)
print('Statistics:')
print('Points average:', average)
grade_dist, failed_course = grades(real_scores)
print('Pass percentage:', pass_percentage(failed_course, len(real_scores)))
print(grade_dist)
