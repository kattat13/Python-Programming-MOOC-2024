from datetime import datetime, timedelta


user_day   = int(input('Day: '))
user_month = int(input('Month: '))
user_year  = int(input('Year: '))

user_dob = datetime(user_year, user_month, user_day)

millennium_eve = datetime(1999, 12, 31)

result = millennium_eve - user_dob

if result.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {result.days} days old on the eve of the new millennium.")