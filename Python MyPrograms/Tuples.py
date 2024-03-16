#Tuples are immutable and lists are mutable
#Tuples are enclosed in () but lists are enclosed in {}

#list_1 = ['coa','os','dsa','dbms']
#list_2 =list_1

#list_1[0] ='probability'

#print(list_1) 
#print(list_2) #assignment is done not of VALUE but REFERENCE /ADDRESS



#Tuples
tuple_1 = ('coa','os','dsa','dbms')
tuple_2 =  tuple_1 

print(tuple_1)
print(tuple_2)
tuple_1[0] ='probability' #ERROR-tuple' object does not support item assignment
print(tuple_1)
print(tuple_2)