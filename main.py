# write your code here 
person = {
           "name":"mariam" ,
            "age" : 16 ,
            "hobbies" :["yoga","art","travel","markting"]  
         }
print(person["name"])
print(person["age"])
person["age"] = 17
person["country"] = "Egypt"
print(person)
print(len(person))
person["hobbies"].append("reading")
print(person)
def check_hobbies(person):
    if len(person["hobbies"])>=3 :
      print("Wow you are amazing")
    else:
       print("error")
check_hobbies(person)
