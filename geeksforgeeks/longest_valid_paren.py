"""

    Original Problem: https://practice.geeksforgeeks.org/problems/longest-valid-parentheses5657/1

"""

# User function Template for Python3
from collections import namedtuple

class Solution:
    """
    Algo:
        1. Get the len of str, `l`,
        2. Push the input char and its position in str, into a stack (list),
           as a tuple
        3. If the current paren is closing paren and prev paren is opening
           paren, pop both the tuple elems.
        4. Repeat steps 1 - 3 for the length of string
        5. For all the remaining elems in the stack, calculate successive diff
           between the char position value and keep track of max diff value.
        6. Also calculate the diff of final pos and length of str.
        7. The max of the values in step 5 and 6 is the answer.
    """
    DEBUG = False

    def _debug(self, *args, **kwargs):
        if self.__class__.DEBUG:
            print(*args, **kwargs)

    def maxLength(self, S):

        PAREN_CLOSE = ')'
        PAREN_OPEN = '('

        l = len(S)

        paren_t = namedtuple('paren_t', ['pos', 'paren'])
        stack = [paren_t(-1, '')]

        for pos_ch_tup in enumerate(S):
            stack.append(paren_t(*pos_ch_tup))
            # self._debug("1. {stack}".format(stack=stack))
            if stack[-1].paren == PAREN_CLOSE and stack[-2].paren == PAREN_OPEN:
                stack.pop()
                stack.pop()

            # self._debug("2. {stack}".format(stack=stack))

        max_len = l - stack[-1].pos
        for i, elem in enumerate(stack):
            if i + 1 < len(stack):
                val = stack[i + 1].pos - elem.pos
                if val > max_len:
                    max_len = val

        return max_len - 1

# {
#  Driver Code Starts
# Initial Template for Python3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends