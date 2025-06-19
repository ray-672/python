class p:
    __pri = 10
    
    def __pm(self):
        print('the number is', p.__pri)


    def pmeth(self):
        p.__pm(self)

ob1 = p()

ob1.pmeth()