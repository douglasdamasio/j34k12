class Server():

    def __init__(self, umax):
        self.users = []
        self.price = 0
        self.umax = umax

    def update(self):
        self.price += 1
        for __user in self.users:
            __user.decrement()
    
    def getTotalTask(self):
        total = 0
        for user in self.users:
            total += user.ttask
        return total

    def is_Empty(self):
        return len(self.users) == 0

    def is_Full(self):
        return len(self.users) == self.umax