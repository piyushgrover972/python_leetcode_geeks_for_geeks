"""
    Original Problem: https://edabit.com/challenge/XhyPkjEDQ3Mz5AFaH
"""
WILD_ZERO_OR_MORE = '*'
WILD_SINGLE_CHAR = '.'
WILDS = WILD_SINGLE_CHAR + WILD_ZERO_OR_MORE


def find_char_pos(string: str, ch: str) -> tuple:
    l = []
    for i, c in enumerate(string):
        if c == ch:
            l.append(i)

    return tuple(l)


def split_strings(string: str, positions: tuple) -> list:
    sub_strs = []
    if (pos := positions[0]) > 0:
        sub_strs.append(string[0:pos])

    for i in range(len(positions) - 1):
        sub_strs.append(string[positions[i]:positions[i + 1]])

    if (pos := positions[-1]) < len(string) - 1:
        sub_strs.append(string[pos:])

    return sub_strs


def dot_match(pat: str, string: str) -> bool:
    pass


def wildcard_match(pattern: str, string: str) -> bool:
    match = False

    wild_pos = find_char_pos(pattern, WILD_ZERO_OR_MORE)
    sub_patterns = split_strings(pattern, wild_pos)

    for sub_pat in sub_patterns:
        if WILD_SINGLE_CHAR not in sub_pat:
            pass

    return match


def is_match(string: str, pattern: str) -> bool:
    if WILD_ZERO_OR_MORE in pattern or WILD_SINGLE_CHAR in pattern:
        return wildcard_match(pattern, string)
    elif string == pattern:
        return True
    else:
        return False