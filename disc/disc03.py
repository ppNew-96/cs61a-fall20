# Write a function that takes two numbers m and n and returns their product.
# Assume m and n are positive integers. Use recursion, not mul or *!

def multiply(m, n):
    min_num = min(m, n)
    max_num = max(m, n)
    def multiply_help(min_num, max_num):
        if min_num == 1:
            return max_num
        else:
            return multiply_help(min_num-1, max_num)+max_num
    return multiply_help(min_num, max_num)

# Recall the hailstone function from Homework 1. Write a recursive version.
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n//2) + 1
    else:
        return hailstone(n*3+1)+1


# Write a procedure merge(n1, n2) which takes numbers with digits in
# decreasing order and returns a single number with all of the digits of the two,
# in decreasing order. Any number merged with 0 will be that number (treat
# 0 as having no digits). Use recursion.

def merge(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1%10<=num2%10:
        return merge(num1//10, num2)*10+num1%10
    else:
        return merge(num1, num2//10)*10+num2%10

# Define a function make fn repeater which takes in a one-argument function
# f and an integer x. It should return another function which takes in one
# argument, another integer. This function returns the result of applying f to
# x this number of times.

def make_func_repeater(f,x):
    def repeat(times, result):
        if times == 0:
            return result
        else:
            return repeat(times-1, f(result))
    return lambda times: repeat(times, x)

# Implement the recursive is prime function.  Do not use a while loop, use recursion.
def is_prime(n):
    def prime_helper(k):
        if k==n:
            return True
        elif n%k==0:
            return False
        else:
            return prime_helper(k+1)
    return False if n == 1 else prime_helper(2)