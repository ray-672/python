w = (0,0,0,1,1,0,1,1,0,1)

s = 0
r = 0

for i in range(0,len(w)):
    if (w[i])==0:
        r +=1

    else:
        s +=1

if (s>=r):
    print('good weather')

else:
    print('bad weather')