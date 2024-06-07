
def balanced_brackets(my_string: str):
    new_str = ''
    for char in my_string:
        if char in '[]()':
            new_str += char
    if len(new_str) == 1:
        return False
    elif len(new_str) == 0:
        return True
    if new_str[0] == '(':
        if not new_str[-1] == ')':
            return False
    elif new_str[0] == '[':
        if not new_str[-1] == ']':
            return False

    # remove first and last character
    return balanced_brackets(new_str[1:-1])


if __name__ == '__main__':
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    ok = balanced_brackets("(x)y)")
    print(ok)