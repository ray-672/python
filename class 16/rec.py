def rec(x):
    
    if x == 0:
        return 1
    else:
        return x *rec(x-1)
    
print(rec(5))
    
    