class Bank():
    crisis=False
    def create_atm(self):
        while not self.crisis :
            yield "$100"


hsbc=Bank()
atm_1=hsbc.create_atm()
print atm_1.next()
print list(atm_1.next() for i in range(5))
hsbc.crisis=True
print atm_1.next()
atm_2=hsbc.create_atm()
print atm_2.next()
hsbc.crisis=False
print atm_1.next()
print atm_2.next()
atm_3=hsbc.create_atm()
print atm_3.next()
