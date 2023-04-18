class prsnl_info:
    last_name = 'Yang'
    height = 'unknown'
    def __init__(self, name):
        self.name = name
        self.age = []
        self.sex = []
    def add_age(self,age):
        self.age.append(age)

    def add_sex(self,sex):
        self.sex.append(sex)

J = prsnl_info('Jerry')
B = prsnl_info('Ben')
M = prsnl_info('Mom')
D = prsnl_info('Dad')

J.add_age(11)
J.add_age(11)
B.add_age(14)
M.add_age('unknown')
D.add_age('unknown')

J.add_sex('Female')
B.add_sex('Male')
D.add_sex('Male')
M.add_sex('Female')

print 'i am a', J.sex
