class pair:
    def tosum(self,tut,target):
        lookup = {}
        sum =0

        for i, val in enumerate(tut):
            sum = sum + val
            lookup[i] = sum
            if sum >= target:
                print('the index is',i, 'for the', target)
                print(lookup)

                return
            
p1 = pair()
tut = (10,20,30,40,50,60,70)

target = 100

p1.tosum(tut,target)