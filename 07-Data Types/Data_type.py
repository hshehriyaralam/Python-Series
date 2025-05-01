#Numeric Data Type
#Integers

int = 42
print("intgers", int)
print(type(int))

#Floating_Numbers
float = 3.142
print("Flaot",float)
print(type(float))
print("hello word for console")

#Complex
complex = 3 + 4j
print(complex)
print(type(complex))


#Accessing Real and Imaginary Parts
rai = 2 + 5j
print("real", rai.real)
print("iamginary", rai.imag)

#Boolean
isActive = True
print(type(isActive))
print("Mode funtions using two integration ")
#str 
text1 = "shahmeer"
text2 = "Sherry893 fjf "
tet5 = "shahmeer Ali Khan"
print(tet5, "tetd,d")
text8 = "sjdcydydcd"
text9 = "Shamehrnhd cnhcha nchjjasn chdhir "
text3 = """jdhioywyodw"""
text4 = '''ndiuqwdiiu'''
print(text1)
print(text1)
print("jjsahf ")
print(text2)
print(text3)
print(text4)


#List
my_list = [1,"JavaScript Array hai", 4,True,3+1j ]
print(type(my_list))
#Python List as JavaSCrpt Array



# Tuple : () use Krte hain 
my_first_tuple = (1,2,3,"tuple",False, 3j+8)
print(type(my_first_tuple))


my_range : range = range(10,2,8)
print(type(my_range))
print(my_range.step)
# range main 3 value hai isko main start, stop and step se get kr sakta hun
# Suppose main range function 4th value pass krun ?? to ye error dega  
# TypeError: range expected at most 3 arguments, got 4


# Set Types 
#Set 
my_set :set = {1,2,44,2,1}
print(type(my_set))
print(my_set)
# Set Dublicate values ko prefere nahi krta 

# Frozent Set 
froz_set : frozenset = frozenset([11,2,3,4,4,5])
print(type(froz_set))
print(froz_set)
# value ko sequence and duplicate value terminate kr dega 



# Dictionary : stored key value pairs 
my_dict : dict = {"name": "Siugt8ww", "age":23 , "languag" : "Marathi"}
print(type(my_dict))
print(my_dict)
# dic as object data type in Python 


# Bytes 
my_bytes :bytes = b"Hello"
print(my_bytes)
print(type(my_bytes))

# WOrking 
with open("Appolo11.jpg", "rb")  as image_file:
    image_data = image_file.read()

print(image_data)    





#Bytearray : Matuable Sequence of Byte 