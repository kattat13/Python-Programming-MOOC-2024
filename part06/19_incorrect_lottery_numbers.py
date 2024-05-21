def validate_week(week: str):
    word, number = week.split(' ')
    if word != 'week':
        return False
    if not number.isdigit():
        return False
    return True
        

def validate_numbers(nums: str):
    num_list = []
    for el in nums.split(','):
        if el.isdigit():
            if int(el) >= 1 and int(el) <= 39:
                num_list.append(el)
    if len(set(num_list)) == 7:
        return True
    return False


def filter_incorrect():
    with open('lottery_numbers.csv') as lottery, open('correct_numbers.csv', 'w') as correct_file:
        for line in lottery:
            week, numbers = line.strip().split(';')
            if validate_week(week) and validate_numbers(numbers):
                correct_file.write(f'{week};{numbers}\n')
                

if __name__ == "__main__":
    filter_incorrect()