from abc import ABC, abstractmethod

class abcc(ABC):

    def print1(self,x):
        print('the valuse is ',x)

    @ abstractmethod

    def tc():

        print('in the abstract class')

class tas(abcc):
    def tc(self):

        print('we are in the inheritad class' )


obj1 = tas()

obj1.print1(200)

obj1.tc()




