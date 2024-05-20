# Write your solution here
def chessboard(n):
    first_row = '1'
    second_row = '0'
    while len(first_row) < n:
        if first_row[-1] == '1':
            first_row += '0'
        else:
            first_row += '1'
    while len(second_row) < n:
        if second_row[-1] == '1':
            second_row += '0'
        else:
            second_row += '1'
    
    counter = 1
    while counter <= n:
        if counter % 2 == 1:
            print(first_row)
        else:
            print(second_row)
        counter += 1 


# Testing the function
if __name__ == "__main__":
    chessboard(3)
