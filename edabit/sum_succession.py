"""
    Original Problem: https://edabit.com/challenge/WoPJpe3RzxGhLSXkv
"""
from utils import Test


def get_numdigs_sum_upto(n_digs: int):
    return sum((10 ** (n_digs - i) - 10 ** (n_digs - i - 1)) * (n_digs - i) for i in range(n_digs))


def concatenation_sum(n: int) -> int:
    """
    Algo:
        1. Find length of num (n), i.e. number of digits 'd'.
        2. Determine largest number with 'd - 1' digits => L = 10^(d - 1) - 1
        3. Find diff => f = n - L
        4. Now, the sum => s1 = f * d, gives us the number of digits in the string formed by all 'd'-digit numbers
           less than or equal to 'n'.
        5. Now, iteratively calculate and sum ((10^(d-i) - 10^(d-i-1)) * (d-i)) for i ∈ [1, d)
        6. This will determine the number of digits in the string formed by all 'd-1', 'd-2', and so on -digits numbers.
    :param n: Max number
    :return: Number of digits in the string, formed by concatenating all the numbers from 1 to n.
    """
    d = len(str(n))
    L = 10**(d - 1) - 1
    f = n - L
    s1 = f * d
    s2 = get_numdigs_sum_upto(d - 1)

    return s1 + s2


if __name__ == '__main__':
    Test.assert_equals(concatenation_sum(1), 1)
    Test.assert_equals(concatenation_sum(9), 9)
    Test.assert_equals(concatenation_sum(10), 11)
    Test.assert_equals(concatenation_sum(999), 2889)
    Test.assert_equals(concatenation_sum(1000), 2893)
    Test.assert_equals(concatenation_sum(4525), 16993)
    Test.assert_equals(concatenation_sum(14122352), 101867713)
    Test.assert_equals(concatenation_sum(114453454235252), 1605690702417684)
    print("Yay!! All tests passed...")