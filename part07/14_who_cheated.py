from datetime import datetime, timedelta


def start_times_dict():
    result = {}
    start_times = open('start_times.csv').read().strip().split('\n')
    for line in start_times:
        name = line.split(';')[0]
        st_time = line.split(';')[1]
        result[name] = datetime(1970, 1, 1,
            hour=int(st_time.split(':')[0]), 
            minute=int(st_time.split(':')[1])
            )
    return result



def cheaters():
    names = []
    start_times = start_times_dict()
    with open('submissions.csv') as file:
        for line in file:
            name = line.split(';')[0]
            submission = line.split(';')[-1]
            sub_date = datetime(1970, 1, 1,
                hour=int(submission.split(':')[0]),
                minute=int(submission.split(':')[1])
            )
            diff = sub_date - start_times[name]
            if diff > timedelta(hours=3) and name not in names:
                names.append(name)
    return names