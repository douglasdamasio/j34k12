class User():
    
    def __init__(self, ttask):
        self.ttask = ttask

    def finish(self):
        return self.ttask == 0

    def decrement(self):
        self.ttask -=1