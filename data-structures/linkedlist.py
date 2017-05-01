#Implementação simples de uma lista encadeada (recursiva?)
#Precisa de melhorias (muito lenta)

class Node(object):
    dado = None
    proximo = None

    def adiciona(self,dado):
        if self.dado is None:
            self.dado = dado
        else:
            if self.proximo is None:
                self.proximo = Node()
                self.proximo.adiciona(dado)
            else:
                self.proximo.adiciona(dado)
    def mostra(self):
        print(self.dado)
        proximo = self.proximo
        while proximo:
            print(proximo.dado)
            proximo = proximo.proximo

a = Node()
a.adiciona('5')
a.adiciona('6')
a.adiciona('7')
a.adiciona('100000')

a.mostra()
            


            



    
        
