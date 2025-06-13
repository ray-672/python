class bird:
    def __int__(self):
        print('the bird is ready')

    def whoisthis(self):
            print('i am a bird!')

class peg(bird):
            def __init__(self):
                super().__init__()
                print('the penguin is ready')

            def who(self):
                super().whoisthis()
                print('i am a penguin!')

p1 = peg()
p1.who()

