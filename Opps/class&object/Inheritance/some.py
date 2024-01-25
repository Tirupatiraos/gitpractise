class ineuron :
    def __init__(self) :
        self.students = "data science"
    
    def student(self) :
        print(self.students)

i = ineuron()
i.student()

i.students = "data analytics"
i.student()


class ineuron1 :
    def __init__(self) :
        self.__students = "data science"
    
    def student(self) :
        print(self.__students)

i1 = ineuron1()
i1.student()

i1.__students = "data scientist"      # here i changed the data but after executing it is not changing gives data science only
i1.student()