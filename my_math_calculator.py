def sqrt(n):
    
    if type(n) not in [int, float]:
        raise TypeError("Parameter must be an int or float.")
    if n < 0:
       raise ValueError("Parameter cannot be a negative number.")

    x = n  # Input is initial approximation.  Could be improved
    y = 1
    e = 0.000001  # accuracy level

    while (x-y > e):
        x = (x + y) / 2
        y = n / x
        
    return x
