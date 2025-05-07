try:
    n = int(input('enter any number:'))

except ValueError as ex:
    print(f'the error is {ex} ')