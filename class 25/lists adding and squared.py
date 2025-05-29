l1 = [3,4,5,6]
l2 = [6,4,3,6]

z = map(lambda x,y:x + y, l1,l2)

print(list(z))

a = [2,3,4,5,6]

def sqr(a):
    return a* a

sq = map(sqr,a)

print(list(sq))