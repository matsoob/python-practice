from collections import deque

class RateLimiter:

    LIMIT = 10

    def __init__(self) -> None:
        self.fifo_queue = deque() #[(0, foo), (5, bar)]
        self.already_logged_set = set() # {foo, bar}

    def log(self, message: str):
        pass

    def log_with_limit(self, timestamp: int, message: str):        
        if self.should_i_log(timestamp, message):
            self.log(message)

    def should_i_log(self, timestamp: int, message: str) -> bool:
        timewindow = timestamp - self.LIMIT
        while self.fifo_queue and self.fifo_queue[0][0] <= timewindow:
            removed = self.fifo_queue.popleft()
            self.already_logged_set.remove(removed)
        
        if message not in self.already_logged_set:
            # IF logging
            self.fifo_queue.append((timestamp, message))
            self.already_logged_set.add(message)
            return True
        return False

# (0, 'foo') true
# (1, 'foo') false
# (5, 'bar') true
# (10, 'foo') false
# (16, 'bar') true
