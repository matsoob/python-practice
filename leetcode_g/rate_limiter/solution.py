# https://leetcode.com/problems/logger-rate-limiter/
from collections import deque


class Logger:

    def __init__(self):
        self.recently_printed = set()
        self.queue = deque()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # (timestamp, 'message')
        # Drain the queue while timestamp >=10 ago
        while self.queue and self.queue[0][0] <= timestamp - 10:
            removed = self.queue.popleft()
            self.recently_printed.remove(removed[1])
        if message in self.recently_printed:
            return False
        else:
            self.queue.append((timestamp, message))
            self.recently_printed.add(message)
            return True

# (10, 'foo')

if __name__ == '__main__':
    logger = Logger();
    assert logger.shouldPrintMessage(1, "foo") == True
    assert logger.shouldPrintMessage(2, "bar") == True 
    assert logger.shouldPrintMessage(3, "foo") == False
    assert logger.shouldPrintMessage(8, "bar") == False
    assert logger.shouldPrintMessage(10, "foo") == False
    assert logger.shouldPrintMessage(11, "foo") == True