'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=[]):
    # Your code here
    a = 0
    b = 0
    c = 1
    total = 1

    for i in range(n):
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
