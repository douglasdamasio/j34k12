# Class Usuário
class User():
    
    # Rebece na inicialização o maximo de tempo de tarefa (ticktask - ttask)
    def __init__(self, ttask):
        self.ttask = ttask

    # Finaliza o tempo de tarefa (ttask)
    def finish(self):
        return self.ttask == 0

    # Decrementa 1 um do ttask
    def decrement(self):
        self.ttask -=1