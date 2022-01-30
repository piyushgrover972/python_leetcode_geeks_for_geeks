from typing import List, Tuple


def print_out_line(test_case_id, outval):
    print(f"Case #{test_case_id}: {outval}")


def get_input():
    inp = []
    test_cases = int(input())
    for i in range(test_cases):
        _, k = input().split()
        s = input()
        inp.append((s, int(k)))

    return inp

def goodness_score(s: str) -> int:
    g = 0
    for i in range(len(s) // 2):
        g += not s[i] == s[-1 - i]
    return g


def min_op_for_goodness(inp: List[Tuple]):
    for i, (s, k) in enumerate(inp):
       print_out_line(i + 1, abs(goodness_score(s) - k))


def main():
    inp = get_input()
    min_op_for_goodness(inp)


if __name__ == '__main__':
    main()
