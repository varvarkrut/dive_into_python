def factorize(x):
    """
    Factorize positive integer and return its factors.
    """
    if not(isinstance(x, int)) or x < 1:
        raise(TypeError)
    divisior = 2
    factors = []
    while (x != 1):
        if x % divisior == 0:
            x = x / divisior
            factors.append(divisior)
        else:
            divisior = divisior + 1
    return(tuple(factors))
