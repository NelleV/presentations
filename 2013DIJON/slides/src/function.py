def fibonacci(n):
    """
    Returns the n-th element of the Fibonacci suite

    Parameter
    ---------
    n : integer
    """
    i = 0
    j = 1
    for it in range(n - 2):
        temp = j
        j = i + j
        i = temp

    return j
