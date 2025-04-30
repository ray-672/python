def cube(x):
    return x*x*x

def divisiblity(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
    
x = float(input('enter the number:'))

res = divisiblity(x)

if res:
    print('yes this is a cube number',res)


else:
    print('no this is not a cubed number')
    