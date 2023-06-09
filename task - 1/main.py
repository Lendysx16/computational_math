import math
import mymath
from prettytable import PrettyTable


eps = 1e-6
c1 = eps / 4.75
c2 = c1 / (2 * 4.2)
c3 = c1 / (2 * 0.9)


def func_my(x):
    res = mymath.cosh_(1 + mymath.sqrt_(1 + x, c2), c1 / 2) * mymath.cos_(mymath.sqrt_(1 + x - x * x, c3), c1 / 2)
    return res


def func_math(x):
    res = math.cosh(1 + math.sqrt(1 + x)) * math.cos(math.sqrt(1 + x - x * x))
    return res


def main():
    result_table = PrettyTable(['x', 'f_exact', 'f_approx', 'error'])
    arguments = [x / 100 for x in range(10, 20 + 1)]
    myres = [func_my(x) for x in arguments]
    mathres = [func_math(x) for x in arguments]

    for x, res1, res2 in zip(arguments, myres, mathres):
        error = abs(res1 - res2)
        result_table.add_row([x, '%.20f' % res2, '%.20f' % res1, '%.20f' % error])
    print(result_table)


if __name__ == "__main__":
    main()
