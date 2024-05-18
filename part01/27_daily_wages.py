# Write your solution here
h_wage = float(input('Hourly wage'))
h_worked = int(input('Hours worked'))
day = input('Day of the week')

wage = h_wage * h_worked * 2 if day == 'Sunday' else h_wage * h_worked

print(f'Daily wages: {wage} euros')