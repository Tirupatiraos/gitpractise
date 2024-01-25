'''if we have same methods in different classess automaticaly it will execute last method because it will override that method.'''
class ineuron :
    def student(self) :
        print("print all the details of the student") 

    def achivers(slef) :
        print("print all the achivers list")
    
    def hall_of_fame(slef) :
        print("print everyone from this group")

class ineuron_vision(ineuron) :

    def student(self):
        print("these are the filter studnets list")


iv = ineuron_vision()
iv.student()