def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

n1 = float(input('enter your first number:'))
n2 = float(input('enter your second number:'))
ch = int(input('enter your choice: \n 1.add \n 2.sub \n 3.mul \n 4.div\n =='))

if ch == 1:
    print(f'{n1} + {n2}={add(n1,n2)}' )


elif ch == 2:
    print(f'{n1} - {n2}={sub(n1,n2)}' )

elif ch == 3:
    print(f'{n1} * {n2}={mul(n1,n2)}' )

elif ch == 4:
    print(f'{n1} / {n2}={div(n1,n2)}' )

else:
    print('this was not an opion')