n = int(input('enter the numer of rows:'))

space = 25

for i in range(1,n+1):
     for k in range(space):
        print(' ', end='')
        for j in range(1,n+1):
            print('*',end=' ')
   
    
        print()

        space -=1


