import operator

def filter_solutions():
    correct = []
    incorrect = []
    operations = {
        '+': operator.add,
        '-': operator.sub
        }

    with open('solutions.csv') as f:
        for line in f:
            problem = line.split(';')[1]
            result = int(line.split(';')[2])

            for op in operations:
                if op in problem:
                    num1, num2 = problem.split(op)
                    if operations[op](int(num1), int(num2)) == result:
                        correct.append(f'{line}')
                    else:
                        incorrect.append(f'{line}')

    with open('correct.csv', 'w') as fc:
        for line in correct:
            fc.write(line)

    with open('incorrect.csv', 'w') as fi:
        for line in incorrect:
            fi.write(line)

if __name__ == "__main__":
    filter_solutions()