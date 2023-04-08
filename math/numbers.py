

# TODO get the set type of number
import math


def get_set_type_of_number(x):
    if x == 0:
        return "Real, Rational, Integer, whole number, Zero"
    elif x > 0 and (x - round(x)) == 0:
        return "Real, Rational, Integer, whole number, Natural"
    elif x < 0 and (x + round(x)) == 0:
        return "Real, Rational, Integer, Negative"
    else:
        return "else"





if __name__ == '__main__':
    print(get_set_type_of_number(math.sqrt(2)))