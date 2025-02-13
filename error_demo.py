""" Errors Found
TypeError  x = "12" + 1
ZeroDivisionError  12 /  0
NameError   return undefined_variable
IndexError  ["a", "b", "c"][100]
AttributeError  ["a", "b", "c"].key()
"""


def calc_square_root(n):
    try:
        from my_math_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt

    answer = sqrt(n)
    return answer


def main():
    in_variable = 1
    try:
        answer = calc_square_root(in_variable)
    except TypeError:
        answer = calc_square_root(float(in_variable))
    except ValueError:
        answer = calc_square_root(abs(in_variable))
    else:
        print("No errors")
    print(answer)


if __name__ == "__main__":
    main()
