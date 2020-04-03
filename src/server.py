# Class Servidor
class Server():

    # Recebe lista de usuários vazia, custo = 0 e o maximo de usuários permitidos
    def __init__(self, umax):
        self.users = []
        self.price = 0
        self.umax = umax

    # Atualiza o custo e abate um tick de tarefa
    def update(self):
        self.price += 1
        for __user in self.users:
            __user.decrement()

    # Pega o tick total da tarefa do usuário
    def getTotalTask(self):
        total = 0
        for user in self.users:
            total += user.ttask
        return total

    # Valida se o servidor está vazio
    def is_Empty(self):
        return len(self.users) == 0

    #  Valida se o servidor está cheio
    def is_Full(self):
        return len(self.users) == self.umax
