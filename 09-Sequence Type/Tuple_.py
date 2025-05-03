# Tupe : Order and immutable collections 

my_tuple = (1,2,3,4)

t1 = (1,2,3) #normal tuple 
t2 = ("ali",2,4,5,"Shahmeer")  # Mixed Tuple
t3 = (5,)  # Single element 
t4 = ([1,3,4,5,6])  #from list 



# access elements
# print(t1[0])
# print(t1[-1])


#For loop 
# for item in t1: 
    # print(item)


#immutable Example 
# t1[1] = 10
# print(t1)
# TypeError: 'tuple' object does not support item assignment


#mthods 
# 1) count() 2) index()

t6 = (2,3,4,3,4,5,6,8)
# print(t6.count(4))
# print(t6.index(2))


#Nested Tuple
t7 = (1,(2,3),7,9,[4,5])
print(t7[1][0])






print(my_tuple)