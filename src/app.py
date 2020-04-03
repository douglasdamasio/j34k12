import sys
from server import Server
from user import User


# Class App (Principal)
class App():

    # Argumentos de inicialização
    def __init__(self, ttask, umax, listConnections):
        self.ttask = ttask
        self.umax = umax
        self.listConnections = listConnections

        self.servers = []
        self.allPrice = 0
        self.outputSystem = []

        self.balaceLogic()

    # Core do App
    def balaceLogic(self):
        for numberConn in self.listConnections:
            for n in range(int(numberConn)):
                self.getServer(self.servers).users.append(User(self.ttask))

            self.updateServers(self.servers, self.outputSystem)
            self.servers = self.deleteServerEmpty(self.servers)
            self.allPrice += len(self.servers)

        while len(self.servers) > 0:
            self.updateServers(self.servers, self.outputSystem)
            self.servers = self.deleteServerEmpty(self.servers)
            self.allPrice += len(self.servers)

        self.outputSystem.append(str(len(self.servers)))

        self.outputSystem.append(str(self.allPrice))

        self.finallyOutput(self.outputSystem)

    # Realiza o output do arquivo
    def finallyOutput(self, __output):
        with open('output.txt', 'w') as file:
            for item in __output:
                file.write(item + '\n')
        file.close()

    # Pega o melhor servidor para processamento da tarefa
    def getServer(self, __servers):
        serverBest = None
        for __server in __servers:
            if not __server.is_Full():
                if not serverBest:
                    serverBest = __server
                elif __server.getTotalTask() > serverBest.getTotalTask():
                    serverBest = __server

        if serverBest:
            return serverBest

        newServer = Server(umax)
        __servers.append(newServer)
        return newServer

    # Atualiza os servidores
    def updateServers(self, __servers, __output):
        amoutUsers = ''
        for __server in __servers:
            __server.users = [
                __user for __user in __server.users if not __user.finish()]

            __server.update()

            if len(__server.users) > 0:
                if amoutUsers != '':
                    amoutUsers += ','
                amoutUsers += str(len(__server.users))

        if amoutUsers != '':
            __output.append(amoutUsers)

    # Elimina o servidor que está vazio
    def deleteServerEmpty(self, __servers):
        return [__server for __server in __servers if not __server.is_Empty()]


# Class de recebimento do arquivo
class ReceptorFile():

    # Arquivo como unico argumento de inicialização
    def __init__(self):
        self.fileInput = sys.stdin

    # Processa o arquivo para devolução das saidas da inicialização do App
    def dataProcessing(self):
        self.listData = []

        for dataLine in self.fileInput:
            try:
                self.listData.append(int(dataLine.strip()))

            except ValueError:
                print('Inválido!\nEspera-se que o arquivo tenha apenas numeros inteiros')
                exit()

            except Exception as e:
                print('Erro:', e)
                exit()

        if len(listData) < 3:
            print('Inválido!\nEspera-se que o arquivo tenha 3 linhas ou mais')
            exit()

        self.ttask = self.listData[0]
        self.umax = self.listData[1]

        if self.ttask >= 1 and self.ttask >= 10:
            print('ttask, não está entre 1 e 10')
            exit()

        if self.umax >= 1 and self.umax >= 10:
            print('umax, não está entre 1 e 10')
            exit()

        self.listData.pop(0)
        self.listData.pop(0)

        return self.ttask, self.umax, self.listData


if __name__ == "__main__":
    ttask, umax, listConnections = ReceptorFile().dataProcessing()
    App(ttask, umax, listConnections)
