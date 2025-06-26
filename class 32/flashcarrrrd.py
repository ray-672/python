class fc:
    def __init__(self,w,m):
        self.w = w
        self.m = m

    def __str__(self):
        return self.w + '('+ self.m +')'
    
fl = []
print("this is the flash card application:")

while(True):
    w = input('enter any word of your choise: \n')

    m = input('enter the meaning of the following word: \n')

    fl.append(fc(w,m))
    op = input('will you contiune y/n?: \n')
    if op.lower() == 'n':
        break

print('these are the flash cards! :> :')
for i in fl:
    print('* ',i)