l = int(input('enter the lovwer range digit:'))
u = int(input('enter the upper range digit:'))

for i in range (l,u+1):
    for j in range (2,i):
        if i%j == 0:
            break
    else:
        print(i)