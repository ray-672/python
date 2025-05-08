import random

c = random.randint(1,10)



while True:
    n = int(input('enter a number:'))

    if n==c:
        print('this is correct!')

        break
    elif c < n:
        print('this number is too high enter a lower number')

    elif c < n:
        print('this number is too low print a higher number')

    