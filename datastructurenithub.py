list_1= ['a', 'b','c', 'd']
list_2= ['boy', 4.8,'True', 30]
print(list_2[-3])
print(list_1[-3])
list_3= ['a', 'b','c', 'd','e','f','g']
print(list_3[::2])
print(list_3[0::2])
print(list_3[0:7:2])

fruits = ['apple' ,'banana' ,'cherry' ,'orange' , 'kiwi' , 'melon' , 'mango']
print(fruits[::-1])
print(fruits.append('mango'))
print(fruits)

list_4= ['a', 'b','c', 'd','e','f','g']
list_4[4:]=1,2,3
list_4[4:]=[1,2,3]
list_4[::2]=1,2,3,4

print(list_4)

list_5 =[1,2,3,4,5,6,7,8,9,10]
list_5[::2]=[None]*5
print(list_5)
list_5[::2]=[0,0,0,0,0]
print(list_5)

list_4.extend(list_5)
print(list_4)


#deleting element(s) of a list 
# #.pop() use when the index known, when the index is not specify the last element is deleted 
# #del
# #.remove()
# #.clear() 
# # lsit packing and unpacking 
# number= list(range(2,21))
# print(number)
# second, forth, sixth, *other, last = number
# print(second)
# print(forth)
# print(sixth)
# print(other)
# print(last)

# #iterate over a list and get the index 
# letters =list("abcd") 
# for index, letter in enumerate(letters):
#     print(index,letter)




# The ord() function is used to get the ASCII code of the character. Example: print(ord('p')) will print 112
print(ord("1"))

print("I", chr(3), "You")
