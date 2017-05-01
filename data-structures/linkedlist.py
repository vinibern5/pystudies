#Implementação simples de uma lista encadeada

class Node(object):
    dado = None
    proximo = None
    ultimo = None

    def adiciona(self,dado):
        if self.dado is None:
            self.dado = dado
        else:
            if self.ultimo is None:
                self.ultimo = Node()
                self.proximo = self.ultimo
                self.proximo.dado = dado
            else:
                self.ultimo.proximo = Node()
                self.ultimo.proximo.dado = dado
                self.ultimo = self.ultimo.proximo
    def mostra(self):
        print(self.dado)
        proximo = self.proximo
        while proximo:
            print(proximo.dado)
            proximo = proximo.proximo

a = Node()


for x in range(1000):
    a.adiciona(x)
    
a.mostra()


            

