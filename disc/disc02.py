# Write a function print delayed that delays printing its argument until the
# next function call. print delayed takes in an argument x and returns a
# new function delay print. When delay print is called, it prints out x and
# returns another delay print

def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Write a function print n that can take in an integer n and returns
# a repeatable print function that can print the next n parameters. After the
# nth parameter, it just prints ”done”.
def print_n(n):
    def inner_print(x):
        if n<=0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

