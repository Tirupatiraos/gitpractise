import ppp1  #if we want to import certain class from other files or moduls 
print(ppp1)  # we have to call like this --> from some1 import person1
obj = ppp1.person1()
print(obj.yob)
class person :
    def __init__(self,name,surname,yob) :
        self.name = name # it is normal variable
        self._surname =surname  #it means protected
        self.__yob = yob   # it means private
sudh = person("tirupati","rao s",2000)
print(sudh.name)
print(sudh._surname)
print(sudh._person__yob)