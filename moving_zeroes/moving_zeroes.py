'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Ok, I had to re-read README and tests a couple more times. And to be honest, I'm still not sure what README means by "Expected Output"
    # Since both sample arrays make it unclear if the output is the qty of non-zero elements, or just simply the highest value in the array
    # However, nowhere do I see in tests where either of these outputs are tested for anyway, so I'll ignore it.
    # What is clear is that the tests show they're looking for non-zero elements all on the left-side of the array, and zeroes all on the right
    # That's it! So I'll loop through the array looking for the zeroes, pop them out and place them at the end.

    # count = len(arr)
    # for x in range(count):
    #     if arr[x] == 0:
    #         arr.pop(x)
    #         arr.append(0)

    # Ok, that didn't work the way I wanted to, and using a while-loop to control iteration created an infinite loop
    # Let's try mapping the elements in the correct order into a temp array

    temp = []
    for x in arr:
        if x == 0:
            # Add to tail of list
            temp.append(0)
        else:
            # Add to head of list
            temp.insert(0, x)

    return temp


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")