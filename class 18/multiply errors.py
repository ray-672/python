try:
    n1, n2 = eval(input('enter two numbers speerated via commas:'))

    r = n1 / n2

    print(f'the result is {r}')

except ZeroDivisionError as z:
    print('the error is a zero divisin error')

except SyntaxError:
    print('the error is a syntax error')

except:
    print('error occour')

else:
    print('no error')

finally:
    print('if there is an error or no error this statment will be executed')