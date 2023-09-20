# You want to go up a flight of stairs that has n steps. You can either take 1
# or 2 steps each time. How many different ways can you go up this flight of
# stairs? Write a function count_stair_ways that solves this problem. Assume
# n is positive.

def count_stair_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return count_stair_ways(n-1) + count_stair_ways(n-2)

# Consider a special version of the count_stairways problem,
# where instead of taking 1 or 2 steps, we are able to take up to and including
# k steps at a time.

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    paths = 0
    for step in range(1, k+1):
        paths += count_k(n-step, k)
    return paths

# Write a function that takes a list s and returns a new list
# that keeps only the even-indexed elements of s and multiplies them by their
# corresponding index.
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [index * s[index] for index in range(len(s)) if index % 2 == 0]


# Write a function that takes in a list and returns the maximum product that
# can be formed using nonconsecutive elements of the list. The input list will
# contain only numbers greater than or equal to 1.
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    keep = s[0] * max_product(s[2:])
    drop = max_product(s[1:])
    return keep if keep > drop else drop