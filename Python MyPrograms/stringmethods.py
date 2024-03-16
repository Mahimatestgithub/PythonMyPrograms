message='Hello World'
print(message.lower())
print(message.upper())
print(message.count('Hello')) #Helko substring is present how much times in string Hello World 
print(message.count('l'))


message='Hello World'
message =message.replace('World','Learners') #replace method does not change original string ,to change original store it in new string 
print(message)

#FORMATTED STRING - CONCAT

greeting = "Hi"
name= "Mahima"
#message1 = greeting+' '+name
#message1 = greeting+', '+name+ '.Welcome!'
#message1 = '{},{}. Welcome!'.format(greeting,name)       #FORMAT {} means placeholder
#message1 = f'{greeting}, {name}.Welcome!'
message1 = f'{greeting}, {name.upper()}.Welcome!'
print(message1)