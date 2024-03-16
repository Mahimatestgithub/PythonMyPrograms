#Dictionary are Key-value pair,like hash maps in java.
#Here key is unique identifier which helps to find data 

#syntax: dict_name ={key:value}
student ={'name': 'Rahul','age': 25, 'courses': ['COA','dS']}
student.update({'name': 'Raj','age': 26, 'phone':12344567890})
print(student)

#del student['age']
#print(student) #deletes the key along with its value 

age=student.pop('age')      #only VALUE is returned from pop function
print(student)
print(age)



print(len(student))  #prints the key-value pairs
print(student.keys())
print(student.values())
print(student.items())      #prints the dictionary item i.e key and its value 





#print(student['name'])
#print(student['courses'])
#print(student['address'])        #KeyError: 'address' since it is not there
#print(student.get('name'))
#print(student.get('phone','Not_Found')) #o/p will be not found 
 
#student['phone']=12344567890    #key along with this value will be added 
#print(student)

#student['name']='Raj' #Rahul will be changed with Raj
#print(student)