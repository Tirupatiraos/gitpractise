class person1 :
    _name = "tiru"
    __surname = "sankrtir"
    yob = 2000

    def _age(self,current_year):
        return current_year - self.yob

obj = person1()
print(obj._age(2023))

class employee(person1) :
    _name  = "pati"
    __surname ="sankr"
    yob = 2003

obj1 = employee()
print(obj1)

print(obj1.yob)
print(obj1._name)
print(obj1._person1__surname)