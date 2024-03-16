courses=['coa','os','dsa','dbms']
print(courses)
print(courses[3])
print(courses[0:3])
print(courses[1:])
print(courses[:2])
 

#courses.append('probabiltiy')
#print(courses)

#courses.insert(0,'probabiltiy') #0 indicates index and probability indicates what to insert 
#print(courses)

#courses.insert(0,['probabiltiy','stats'])  #multiple indices to be inserted ,it goes to same index 0
#print(courses)

#courses=['coa','os','dsa','dbms']
#courses2=['probabiltiy','stats']
#courses.extend(courses2)   #EXTEND puts the element at NEW INDEX 
#print(courses)

#courses.remove('os')
#print(courses)

#courses.pop()          #POP removes the last element
#print(courses)

#popped_item = courses.pop()          #POP removes the last element and printing it here 
#print(courses)
#print(popped_item)

print(courses.index('os'))
print('os' in courses)
print ('cn' in courses)

courses.reverse()
print(courses)

courses.sort()    #Sorted in ascending order 
print(courses)

nums=[ 2,5,4,6,1]
#nums.sort()
#nums.sort(reverse=True)
#print(nums)

sorted_nums =sorted(nums)    
print(nums)              #it will print original nums
print(sorted_nums)   #it will print sorted nums














#courses1=['coa','os','dsa',['dbms','cn']]
#(len(courses1))
#print(courses1[3])
#print(courses1[3][0]) #o indicated index no i.e dbms
#print(courses1[3][1])    #1 indicated index no i.e cn
  