class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def dis(self):
        print('the name is',self.name)
        print('the id is',self.id)

class emp(person):
        def __init__(self,name,id,salary,post):
            person.__init__(self,id,name)
            self.salary = salary
            self.post = post

        def disp(self):
            person.dis(self)
            print('the salary is',self.salary)
            print('the post is', self.post)

e = emp(1234,'mike',30000,'superviser')
e.disp()
    