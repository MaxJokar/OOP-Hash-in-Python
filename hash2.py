#Objects can be Hashable using Hash def(Everything has a HASH code)
class Person:

    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
  
#To avoid equal objects we use the following Method
#self is p1 and object2 is p2,p3p4       
    def __eq__(self, obj2):
        if not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self.__age==obj2.__age #Brings True oR False:
           
    
#Sets to contain their content ,use from Hash of a  contenct
#Objects dont have hash , unlikely numbers, strings and decimals
#the Below hash function can  return the and Objects hash as well    
    def __hash__(self) -> int:
        return hash(self.__name)+hash(self.__age)
    
    def __str__(self):
        return f"Name is  :{self.__name}\t Age is :{self.__age}"
    
    
    
p1=Person("Jack",15)
p2=Person("Andy",14)
p3=Person("Dany",35)
p4=Person("Jack",15)


set1={p1,p2,p3,p4}
for person in set1:
    print(person)

list1=[p1,p2,p3,p4]
for person in list1:
    print(person)