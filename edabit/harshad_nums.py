"""
    Original Problem: https://edabit.com/challenge/gXwRi9orArjTKxRJL
"""

from typing import List


class Harshad:

    def __init__(self, seed):
        assert seed > 0, "A Harshad number must be +ve"
        if self.is_harshad(seed):
            self._nums = [seed]
            return
        self._nums = []

    def __len__(self):
        return len(self._nums)

    def index(self, num):
        try:
            return self._nums.index(num) + 1
        except ValueError:
            return 0

    def is_harshad(self, num: int) -> bool:
        return num > 0 and (num % sum(self._get_digits(num))) == 0

    @staticmethod
    def _get_digits(num: int) -> List[int]:
        return list(map(int, list(str(num))))

    def next(self):
        if self._nums and self.is_harshad(num := self._nums[-1] + 1):
            self._nums.append(num)
            return num
        else:
            raise StopIteration

    def prev(self):
        if self._nums and self.is_harshad(num := self._nums[0] - 1):
            self._nums.insert(0, num)
            return num
        else:
            raise StopIteration

    def __str__(self):
        return f"Harshad({self._nums})"

    @property
    def numbers(self):
        return self._nums


def find_harshad_sequence(n):
    h = Harshad(n)

    stop = 0
    while True:
        try:
            h.next()
        except StopIteration:
            break
    while True:
        try:
            h.prev()
        except StopIteration:
            break

    print(h)

    return h


def harshad(n):
    hseq = find_harshad_sequence(n)

    return [len(hseq), hseq.index(n)]

