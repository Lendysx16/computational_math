def sqrt_(x, eps):
    sign = x < 0
    x = abs(x)
    x_n = 1.0
    result = 0
    error = 999999999999999
    while error > eps:
        result = 0.5 * (x_n + x / x_n)
        error = abs(result - x_n)
        x_n = result
    if sign:
        result = -result
    return result


def pow_(x, n):
    start_x = x
    k = 1
    while k < n:
        if k + k <= n:
            x *= x
            k += k
        else:
            x *= start_x
            k += 1
    return x


def cos_(x, eps):
    result = 1
    x_n = 1.0
    sqr_x = x * x
    i = 0.0
    while abs(x_n) > eps:
        i += 2
        x_n *= -sqr_x / (i - 1) / i
        result += x_n
    return result


def cosh_(x, eps):
    result = 1.0
    x_n = 1.0
    i = 0.0
    sqr_x = x * x
    while abs(x_n) > eps:
        i += 2
        x_n *= x * x / (i - 1) / i
        result += x_n
    return result

