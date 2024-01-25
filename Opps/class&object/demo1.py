class person :
   def __init__(tiru,name,surname,emailid,dob) :
      tiru.name = name 
      tiru.surname = surname
      tiru.emailid = emailid 
      tiru.dob = dob 
obj = person("anuj","bandati","anuj@gmail.com",2010)
obj1 = person("tiru","pati","tiru@gmail.com",2000)
obj2 = person("tirupati","sankrtir","tirpati@gmail.com",3023)
print(obj.name)
print(obj1.dob)
print(obj2.emailid)