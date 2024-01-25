class person :
   def __init__(self,name,surname,emailid,dob) :
      self.name = name 
      self.surname = surname
      self.emailid = emailid 
      self.dob = dob 
# calculating age of a person
   def age(tiru,current_year):
      return current_year-tiru.dob

obj = person("anuj","bandati","anuj@gmail.com",2010)
obj1 = person("tiru","pati","tiru@gmail.com",2000)
obj2 = person("tirupati","sankrtir","tirpati@gmail.com",3023)
print(obj1.age(2023))
