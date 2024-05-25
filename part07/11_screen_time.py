from datetime import datetime, timedelta


def collect_data():
    screen_time_dict = {}
    print('Please type in screen time in minutes on each day (TV computer mobile):')
    for i in range(n_days):
        new_date = start_date + timedelta(days=i)
        user = input(f'Screen time {new_date.strftime("%d.%m.%Y")}: ')
        screen_time_dict[new_date.strftime("%d.%m.%Y")] = user
    return screen_time_dict


def calc_stats(screen_time: dict):
    total_minutes = 0
    for _, value in screen_time.items():
        list_of_nums = value.split(' ')
        for x in list_of_nums:
            total_minutes += int(x)
    return total_minutes


filename   = input('Filename: ')
user_date  = input('Starting date: ')
n_days     = int(input('How many days: '))

# filename   = 'late_june.txt'  # input('Filename: ')
# user_date  = '24.6.2020'  # input('Starting date: ')
# n_days     = 5  # int(input('How many days: '))

try:
    start_date = datetime.strptime(user_date, "%d.%m.%Y")
except Exception as e:
    print(e)

last_date = start_date + timedelta(days=n_days-1)
header = f'Time period: {start_date.strftime("%d.%m.%Y")}-{last_date.strftime("%d.%m.%Y")}\n'

data = collect_data()

total_minutes = calc_stats(data)
average_minutes = total_minutes / n_days

with open(filename, 'w') as f:
    f.write(header)
    f.write(f'Total minutes: {total_minutes}\n')
    f.write(f'Average minutes: {average_minutes}\n')
    for key, value in data.items():
        f.write(f"{key}: {value.replace(' ', '/')}\n")

print(f'Data stored in file {filename}')
