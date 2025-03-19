cp = float(input('please enter your cost price:'))
sp = float(input('please enter your sellling price:'))

if sp > cp:
    amt = sp - cp
    print('you made profit!!: {0}'. format(amt))

else:
    amt = cp - sp
    print('your profit is nothing...:{0}'. format(amt))

