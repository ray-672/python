class ioostring:
    def __init__(self):
        self.str1 = ''

    def getstr(self):
        self.str1 = input('enter the string:')

    def uppstr(self):
        print(f'the upper case of {self.str1} is {self.str1.upper()}')

odj = ioostring()
odj.getstr()
odj.uppstr()
        