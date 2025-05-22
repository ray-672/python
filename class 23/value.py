
key1 = {'codingal':3,'is':3,'the best':2,'coding':2}

k = 2
result = 0
for value in key1:
    if key1[value] == 2:
        result +=1

print(f'the count is {result}')