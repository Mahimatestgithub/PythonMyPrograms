# and
# or 
# not
 
# ==
# !=
# >
# >=
# <
# <=
# is     is ->used for object Identity comparisons since == compares only VALUE

#Object Identity: is 

# list1=[1,2,3]
# list2=[1,2,3]

# print(list1)
# print(list2)

# print(list1==list2)
# print(list1 is list2) #since both the list objects are different,returns false


# print(id(list1))
# print(id(list2)) #both have different id's

list1=[1,2,3]
list2=list1

print(id(list1))
print(id(list2))

print(list1 is list2)




























#AND CASE
# user='mahima'
# logged_in =True

# if user=='mahima' and logged_in:
# 	print('Mahima Page')
# else:
# 	print('Wrong credentials')

# user='mahima'
# logged_in =False

# if user=='mahima' and logged_in:
# 	print('Mahima Page')
# else:
# 	print('Wrong credentials')


# NOT CASE
user='mahima'
logged_in =False
if not logged_in:
	print('please log_in')
else:
	print('Welcome!')

















