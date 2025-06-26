class a:
    def __init__(self,x):
        self.x = x

    def __lt__(self,otr):
        if self.x < otr.x:
            return 'ob1 is less then ob2'
        
        else:
            return 'ob2 is less then ob1'
        

    def __eq__(self,otr):
        
        if self.x == otr.x:
    
            return 'ob1 is  equal ob2'
    

        else:
            return 'ob1 is NOT equal to ob2'
        

ob1 = a(10)
ob2 = a(30)

print(ob1<ob2)

print(ob1 == ob2)