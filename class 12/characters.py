str1 = input('enter a phrase or word of your choice:')

ch = input('enter the charactor of uour choice:')

count = 0

for i in str1:
    if i ==ch:
        count+=1
print(f'the amount of characters in {str1} is {count}')
