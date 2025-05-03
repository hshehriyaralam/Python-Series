# Sequence Data Type 
# 1) string  "" 
# 2) list  []
# 3) Tuple  ()


# String  assign with single and double qoutations
# my_name = "shahmeer"
# print(my_name)


#list  : ordered and Mutubale Collecton
# fruits = ["appple", "mango", "Banan" , "Ornge"]

# print(fruits)
# fruits[-1] = "Orange"
# print(fruits)

#add Items 
# fruits.append("Milk")
# print(fruits)
# fruits.insert(0,"Tamato")
# print(fruits)


#Remove items
# fruits.remove("Milk")
# fruits.pop()  #remove last index
# del fruits[0]
# print(fruits)


#Loop apply 
# for item in fruits :
#    print(item)



#Usefull Methods 
Cities = ["Karachi", "Islamabad", "Multan", "Rawalpindi","Islamabad"]
print(Cities)
# Cities.append("Faislabad")
# Cities.insert(2, "Skkhar")
# Cities.pop()
# Cities.remove("Rawalpindi")
# Cities.clear()
# print(Cities.count("Islamabad")) # || Value ko pata kr sakte ke ktni duplicate values hai 
# Cities.reverse() # lsi order ko revers kr dega 
# Cities.sort()  #|| order sequence karega alphate and ascending 
# copy_list = Cities.copy()
# copy_list.append("Kashmir")
# print(copy_list)

IndianCities = ["Mumbai", "Dehli", "Panjab"]
print(IndianCities)
Cities.extend(IndianCities)










print(Cities)