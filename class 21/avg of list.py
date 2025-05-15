l = [1,3,6,9,2,10,5]
print('the original list is:',l)

sum = 0

for i in l:
    sum+=i

avg = sum/len(l)
print('the avg is:',avg)
print('the sum is:',sum)

print('the minimum number is:',min(l))
print('the maximum is:',max(l))