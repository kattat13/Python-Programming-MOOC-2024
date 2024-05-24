from datetime import datetime


def check_date(date_of_birth, marker):
    if marker == '+':
        year = 1800
    elif marker == '-':
        year = 1900
    else:
        year = 2000
    day = int(date_of_birth[0:2])
    month = int(date_of_birth[2:4])
    year += int(date_of_birth[4:])
        
    try:
        dob = datetime(year, month, day)
    except Exception as exc:
        # print(exc)
        return False
    return True
    

def check_marker(century_marker):
    valid_markers = ['+', '-', 'A']
    if century_marker in valid_markers:
        return True
    

def calc_control(pic):
    CHARS = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    digits_only = int(''.join([x for x in pic[:-1] if x.isdigit()]))
    rem = digits_only % 31
    return CHARS[rem]


def is_it_valid(pic: str):
    if len(pic) == 11:
        marker = check_marker(pic[6])
        if marker:
            dob = check_date(pic[:6], pic[6])
            if dob:
                control = calc_control(pic)
                if control == pic[-1]:
                    return True
    return False

if __name__ == "__main__":
    # print(is_it_valid('081142-720N'))
    # print(is_it_valid('100400A644E'))
    print(is_it_valid('130767-6199'))
