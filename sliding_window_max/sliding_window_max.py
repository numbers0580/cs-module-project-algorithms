'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max_first_attempt(nums, k):
    # Your code here
    # What's clear to me is that any loop used can only go from 0 to len() - k, assuming the array has len() > k
    # Otherwise, no loop is needed if len() <= k

    output = [0] * ((len(nums) - k) + 1) # This might cause an error if k > len(). I probably should just use output = [] and append answers instead

    if len(nums) <= k:
        # One pass -- and thus one element -- only
        maxvalue = nums[0] # initialized to first element in case of negative values
        for i in nums[1:]:
            # Starting from 2nd element in array
            if i > maxvalue:
                maxvalue = i

        output[0] = maxvalue
    else:
        iterations = len(nums) - k + 1
        for x in range(iterations):
            maxvalue = nums[x] # initialized to first element of this window in case of negative values

            for y in range(k):
                if nums[x + y] > maxvalue:
                    maxvalue = nums[x + y]

            output[x] = maxvalue

    # This works well for the normal test, but I calculate it would take approximately 18 hours to complete the large_input test using the above method
    return output



def sliding_window_max(nums, k):
    # This time, I'll ignore the if-else statement (since none of the tests ever went to the if part)
    # and utilize array slicing and python's max function for numpy arrays
    output = [0] * (len(nums) - k + 1)

    for z in range(len(nums) - k + 1):
        window = nums[z:z + k]
        maxval = max(window)
        output[z] = maxval

    # This version was only about 3 times faster than my original version with the nested for-loop. That means it would've still taken about 6 hours to complete the large file
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
