def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    m = 1
    for i in range(n, n-k, -1):
        m = m*i
    return m

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    x = y
    n = 0
    while x != 0:
        x = x // 10
        n += 1
    sum = 0
    for i in range(n, 1, -1):
        s = y // 10**(i-1)
        y -= s * 10**(i-1)
        sum += s
    sum += y
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    x = n
    y = 0
    while x != 0:
        x = x // 10
        y += 1
    t = False
    for i in range(y, 1, -1):
        if (n % 10**(i)) // 10**(i-2) == 88:
            t = True
    return t
