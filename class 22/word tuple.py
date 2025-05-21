def check(a):
    le = len(a)

    start = 0
    end = le-1

    while start < end:
        if a[start] != a[end]:
            return False
        
        start +=1
        end -=1

    return True

a = (1,2,3,4,3,2,1)

if check(a):
    print('this is a palindrone')
else:
    print('this is not a palindrone')