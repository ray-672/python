class em:
    def __init__(self):
        print('enployee was created')

    def __del__(self):
        print('employee was deleted')

el = em()

print('this is in the middle')

del(el)

e2 = em()
