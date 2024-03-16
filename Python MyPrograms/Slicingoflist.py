list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print(list[-6])
print(list[0:5])
print(list[-10:-6])
print(list[:6])   #prints from 0 to 5
print(list[4:])    #prints from 4 to 9
print(list[7:3])    #no o/p i.e,[] since we are coming from back to front
print(list[-3:-8])   #no o/p i.e,[] since we are coming from back to front

#list[start:end:step]
print(list[-3:-8:-1]) #from 7 to 3 will be printed and 2 will not be printed as step is -1
print(list[-3:-8:-2])  #it will take shift of +2 so prints 7,5,3
print(list[0:10:2])
print(list[9::2])
print(list[9::-2])
print(list[::1]) # +1 does it 
print(list[::-1]) #