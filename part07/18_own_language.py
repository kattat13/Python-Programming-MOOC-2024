from string import ascii_uppercase

def basic_commands():
    pass


def run(program):
    
    variables = dict.fromkeys(ascii_uppercase, 0)
    printed = []
    
    for line in program:
        if line.split(' ')[0] == 'END':
            return printed
        if line.split(' ')[0] == 'PRINT':
            printed.append(variables[line.split(' ')[1]])
        else:
            command, variable, value = line.split(' ')
            if command == 'MOV':
                if value.isdigit():
                    variables[variable] = int(value)
                else:
                    variables[variable] = variables[value]
            elif command == 'ADD':
                if value.isdigit():
                    variables[variable] += int(value)
                else:
                    variables[variable] += int(variables[value])
            elif command == 'SUB':
                if value.isdigit():
                    variables[variable] -= int(value)
                else:
                    variables[variable] -= int(variables[value])
            elif command == 'MUL':
                if value.isdigit():
                    variables[variable] *= int(value)
                else:
                    variables[variable] *= variables[value]

    return printed


if __name__ == '__main__':
    program1 = []
    # program1.append("MOV A 10")
    # program1.append("MOV B 2")
    program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    program1.append("END")
    # program1.append("MOV B A")
    # program1.append("SUB B 8")
    # program1.append("PRINT B")
    # program1.append("SUB A B")
    # program1.append("PRINT A")
    result = run(program1)
    print(result)