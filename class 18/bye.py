flag = False

while not flag:
    try:
        n = int(input('enter any number'))
        if n%2 ==0:
            print('bye bye')

        else:
            flag = True

    except ValueError:
        print('there is an error')
