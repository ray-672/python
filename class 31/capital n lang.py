class India:
    def cap(self):
        print('the capital of India is NewDelhi')

    def lang(self):
        print('the most common language spoken is Hindi')

class Sri_lanka:
    def cap(self):
        print('the capital of Sri lanka is colombo')

    def lang(self):
        print('the most common language spoken is Sinhala')


ob1 = India()
ob2 = Sri_lanka()

for x in [ob1,ob2]:
    x.cap()
    x.lang()
