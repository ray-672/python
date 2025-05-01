str1 = input('enter a phrase of your choice:')

for i in str1:
    if i.lower() == 'a' :
        print('there is an a in the phrase {str1}')
        break
else:
     print('there is not an a in the phrase {str1}')