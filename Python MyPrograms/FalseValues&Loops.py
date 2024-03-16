# False Values:
# 1.False
# 2.None
# 3.Zero or any numeric type
# 4.Any empty sequence.For example, '',(),[].
# 5.Any empty mapping.For example,{}.

condition= None
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')


#Loops
# nums =[1,2,3,4,5]
# for num in nums:
# 	print(num)


# student ={'name': 'Rahul','age': 25, 'courses': ['COA','dS']}
# #for key in student:
# for key,value in student.items():
# 	print(key,value)

#break and continue
nums=[1,2,3,4,5]
for num in nums:
	if num==3:
		print('Found')
		break
		#continue
	print(num)

#loop in range 
# for i in range(10):
# 	print(i)

# for i in range(1,10):  #1 is imclusive but 10 is exclusive so it prints from 1 to 9
# 	print(i)


#Loops in Loops
nums=[1,2,3,4]
for num in nums:
	  for letter in 'abc':
	  	print(num,letter)


#While loops,here we have to mention initialisation,condition,updation
x=0;
while x<10:
	print(x)
	x+=1










