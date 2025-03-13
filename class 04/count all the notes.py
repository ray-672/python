amount = int(input('how much money would you like to take?:'))

note1 = (amount//100)
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print('the number of hundred notes:',note1)
print('the number of 50 notes', note2 )
print('number of 10 notes', note3)
