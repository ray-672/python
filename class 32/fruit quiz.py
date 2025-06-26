import random

class fq:
    def __init__(self):
        self.d1 = {
            'apple':'red',
            'banana':'yellow',
            'grape':'purple',
            'orange':'orange',
            'blueberry':'blue',
            'watermelon':'green'
        }

    def qu(self):
        while True:
            fruit,colour = random.choice(list(self.d1.items()))

            print('what is the colour of...:',fruit)

            u = input('what is the colour?:')

            if u.lower() == colour:
                print('correct! ;>')
            else:
                print('wrong!')
            c = input('do you want to play again?: y or no')
            if c.lower() == 'n':

                break

ffq = fq()
ffq.qu()