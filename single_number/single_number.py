'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # So both the array below and the constructed one in the test file are not sorted
    # I think a portion of the count sort method would apply here

    count = [0] * len(arr) # I know this is practically twice as long as we need, but I'll ignore the 0's at the end

    for i in arr:
        count[i] += 1

    pos = 0
    while count[pos] != 1 and pos < len(arr):
        pos += 1

    return pos



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")