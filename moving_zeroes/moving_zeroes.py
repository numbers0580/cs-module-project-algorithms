'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # If I understand the README, I may need a temporary array to house only the non-zero integers
    # I can't pop the zeroes out of arr because it appears the README shows the original array length doesn't change

    temp = []

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")