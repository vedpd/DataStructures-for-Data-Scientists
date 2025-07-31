class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.runningSum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.runningSum += val

        if len(self.queue) > self.size:
            self.runningSum -= self.queue.popleft()
        
        return self.runningSum / len(self.queue)  #dividing by self.queue and not size as initially queue can have just 1 element itself and then average is that number / 1

        

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)