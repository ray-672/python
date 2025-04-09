n = int(input('enter any number of your choice:'))
num = n
rev = 0

while num > 0:
    rem = num%10
    rev += rem**3
    num//= 10
    print(rev)

if n == rev:
    print(n,'this number is an armstrong number')
else:
    print(n,'this is not an armstrong number')
