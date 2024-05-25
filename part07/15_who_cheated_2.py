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


def calc_sum(final_points: dict):
    points_sum = {}
    for key, value in final_points.items():
        points_sum[key] = 0
        for _, points in value.items():
            points_sum[key] += points
    return points_sum


def final_points():
    final_points_dict = {}
    start_times = start_times_dict()
    with open('submissions.csv') as file:
        for line in file:
            name = line.split(';')[0]
            exercise = int(line.split(';')[1])
            points = int(line.split(';')[2])
            submission = line.split(';')[-1]
            sub_date = datetime(1970, 1, 1,
                hour=int(submission.split(':')[0]),
                minute=int(submission.split(':')[1])
            )
            diff = sub_date - start_times[name]
            if diff < timedelta(hours=3):
                temp_dict = {}
                temp_dict[exercise] = points
                if name in final_points_dict:
                    if exercise in final_points_dict[name]:
                        if final_points_dict[name][exercise] < points:
                            final_points_dict[name][exercise] = points
                    else:
                        final_points_dict[name].update(temp_dict)
                    
                else:
                    final_points_dict[name] = temp_dict
    points_sum = calc_sum(final_points_dict)
    return points_sum


if __name__ == "__main__":
    print(final_points())