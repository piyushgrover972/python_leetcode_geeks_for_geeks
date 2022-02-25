"""
    https://leetcode.com/problems/divisor-game/

    Tags: Google Assessment; Dynamic Programming; Easy;
"""


class Solution:
    def __init__(self):
        self.primes = [1]
        self.dp_cache = {}

    def seive(self):
        arr = [1] * 1001

        j = 2
        while j < len(arr):

            if arr[j]:
                self.primes.append(j)

                k = j + j
                while k < len(arr):
                    arr[k] = 0
                    k += j

            j += 1

    def dp_game(self, n: int) -> bool:

        if n == 1:
            return False

        if n in {0, 2}:
            return True

        elif n not in self.dp_cache:
            if n in self.primes:
                self.dp_cache[n] = not self.dp_game(n - 1)
            else:
                self.dp_cache[n] = False
                for k in self.primes:
                    if n % k == 0:
                        self.dp_cache[n] = not self.dp_game(n - k) or not self.dp_game(n - (n // k))

                        if self.dp_cache[n]:
                            break
                    if k > n // 2:
                        break

        return self.dp_cache[n]

    def divisorGame(self, n: int) -> bool:
        self.seive()
        return self.dp_game(n)
