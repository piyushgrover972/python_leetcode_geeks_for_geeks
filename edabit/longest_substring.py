"""
    Original Problem: https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
"""

import re


def remainder(divisor):
    def _find_rem(dividend):
        return dividend % divisor
    return _find_rem


def span_len(span: tuple[int, int]) -> int:
    return span[1] - span[0]


def longest_substring(digits: str) -> str:
    if len(digits) < 2:
        return ''

    # Find the remainder string
    remainder_str = ''.join(map(str, map(remainder(2), map(int, digits))))

    # Match multiple occurences (at least 1) of '01' followed by at most single '0' (if any)
    # Or similarly,
    # Match multiple occurences (at least 1) of '10' followed by at most single '1' (if any)
    pat = r"((?:01)+0?)|((?:10)+1?)"

    max_len_span = ()
    max_len = 0
    for match in re.finditer(pat, remainder_str):
        if max_len < (spln := span_len(spn := match.span())):
            max_len = spln
            max_len_span = spn

    return digits[max_len_span[0]:max_len_span[1]]


class Test:
    @classmethod
    def assert_equals(cls, func_out: str, expected_out: str):
        assert func_out == expected_out, f"Function output '{func_out}' != Expected output '{expected_out}'"


if __name__ == '__main__':

    # Test Cases copied from edabit's problem's test cases
    Test.assert_equals(longest_substring("844929328912985315632725682153"), "56327256")
    Test.assert_equals(longest_substring("769697538272129475593767931733"), "27212947")
    Test.assert_equals(longest_substring("937948289456111258444958189244"), "894561")
    Test.assert_equals(longest_substring("736237766362158694825822899262"), "636")
    Test.assert_equals(longest_substring("369715978955362655737322836233"), "369")
    Test.assert_equals(longest_substring("345724969853525333273796592356"), "496985")
    Test.assert_equals(longest_substring("548915548581127334254139969136"), "8581")
    Test.assert_equals(longest_substring("417922164857852157775176959188"), "78521")
    Test.assert_equals(longest_substring("251346385699223913113161144327"), "638569")
    Test.assert_equals(longest_substring("483563951878576456268539849244"), "18785")
    Test.assert_equals(longest_substring("853667717122615664748443484823"), "474")
    Test.assert_equals(longest_substring("398785511683322662883368457392"), "98785")
    Test.assert_equals(longest_substring("368293545763611759335443678239"), "76361")
    Test.assert_equals(longest_substring("775195358448494712934755311372"), "4947")
    Test.assert_equals(longest_substring("646113733929969155976523363762"), "76523")
    Test.assert_equals(longest_substring("575337321726324966478369152265"), "478369")
    Test.assert_equals(longest_substring("754388489999793138912431545258"), "545258")
    Test.assert_equals(longest_substring("198644286258141856918653955964"), "2581418569")
    Test.assert_equals(longest_substring("643349187319779695864213682274"), "349")
    Test.assert_equals(longest_substring("919331281193713636178478295857"), "36361")

    print("All Tests Passed !!")


