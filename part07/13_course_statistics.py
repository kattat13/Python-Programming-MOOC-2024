import urllib.request
import json
from math import floor


def retrieve_course(course_name: str):
    address = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    response = urllib.request.urlopen(address).read()
    data = json.loads(response)

    result = {}
    result['weeks'] = len(data)
    result['students'] = 0
    result['hours'] = 0
    result['exercises'] = 0
    for _, x in data.items():
        if x['students'] > result['students']:
            result['students'] = x['students']
        result['hours'] += x['hour_total']
        result['exercises'] += x['exercise_total']
    result['hours_average'] = floor(result['hours'] / result['students'])
    result['exercises_average'] = floor(result['exercises'] / result['students'])

    return result


def retrieve_all():
    response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses").read()
    data = json.loads(response)
    result = []
    for x in data:
        if x['enabled'] == True:
            result.append((x['fullName'], x['name'], x['year'], sum(x['exercises'])))
    return result


if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course('docker2019'))