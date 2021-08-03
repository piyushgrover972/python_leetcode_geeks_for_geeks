"""
    Original Problem: https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
"""


def is_odd(num: int) -> bool:
    return num % 2 == 1


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_all_odd(nums: list[int]):
    return all(map(is_odd, nums))


def is_all_even(nums: list[int]):
    return all(map(is_even, nums))


def remainder(divisor):
    def _find_rem(dividend):
        return dividend % divisor
    return _find_rem


def longest_substring(digits: str) -> str:
    if len(digits) < 2:
        return ''
    substr_len_pos_map = {}

    # Find the remainder string
    remainder_str = ''.join(map(str, map(remainder(2), map(int, digits))))

    pat = r"((?:01)+0?)|((?:10)+1?)"
    pos = 0
    while pos < len(remainder_str):
        pass



