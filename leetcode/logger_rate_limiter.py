"""
    https://leetcode.com/problems/logger-rate-limiter/

    Tags: Google; Easy
"""


class Logger:

    def __init__(self):
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message not in self.last_printed) or (
                message in self.last_printed and self.last_printed[message] + 10 <= timestamp):
            self.last_printed[message] = timestamp
            return True

        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
