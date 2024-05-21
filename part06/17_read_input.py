def read_input(command, lower_limit, higher_limit):
    while True:
        try:
            user = int(input(command))
        except ValueError:
            print(f'You must type in an integer between {lower_limit} and {higher_limit}')
            continue
        if user > int(lower_limit) and user < int(higher_limit):
            return user
        else:
            print(f'You must type in an integer between {lower_limit} and {higher_limit}')





if __name__ == "__main__":

    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)