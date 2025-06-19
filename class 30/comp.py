class comp:
    def __init__(self):
        self.__mp = 1000

    def smp(self,pri):
        self.__mp = pri

    def display(self):
        print('the max price is',self.__mp)

c1 = comp()
c1.__mp = 2020
c1.display()
c1.smp(2222)
c1.display()
