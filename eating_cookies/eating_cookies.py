import math

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=[]):
    # Your code here
    total = 0

    if n < 3:
        total = math.factorial(n)
    else:
        a = math.factorial(0) # 1
        b = math.factorial(1) # 1
        c = math.factorial(2) # 2
        # Note: Simple factorials won't work beyond n = 2
        for i in range(n-2):
            total = a + b + c
            # Shift a, b, and c for next iteration of for-loop
            a = b
            b = c
            c = total

    return total


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    # General Note: Based on what I discovered about this problem, I decided to expand further for all possible permutations
    # of all possible simultaneous quantities of cookies that Cookie Monster would eat:
    # If up to 2 cookies at a time: Fibonacci recursion: k[x] = k[x-1] + k[x-2]
    # If up to 3 cookies at a time (this problem): Tribonacci recursion: k[x] = k[x-1] + k[x-2] + k[x-3]
    # If up to 4 cookies at a time: Quadronacci (is that a word?) recursion: k[x] = k[x-1] + k[x-2] + k[x-3] + k[x-4]
    # If up to n cookies at a time: k[x] = k[x-1] + k[x-2] + k[x-3] + k[x-4] + ... + k[x-n]
