from functools import reduce
# File handling : Read/Write/Append/Binary

with open("file handling.txt","r") as source_file:
    select =source_file.readlines()
    print(source_file.readline()) #readline will not work here, as readlines() could have made the pointer to the end of the file
    # Thus readline() doesn't have anything to read really

with open("file handling copy.txt","w") as target_file: #"With" will close the file automatically
    for data in select:
        print(data)
        target_file.write(data)

# Always make sure to close the file,if this file is opened anywhere above
with open("file handling copy.txt","r") as copied_file:
    print(copied_file.read())

# Write method completely rewrites the file, thus if you wanna append something to a file , use append mode 
with open("file handling copy.txt","a") as appending_file:
    appending_file.write("\nI am enthusuastic")

# Opening and copying a image file
with open("Virat-Kohli.png","rb") as src_img:
    image=src_img.read() #Displays the binary data 

with open("Virat-Kohli-cp.png","wb") as tgt_img:
        tgt_img.write(image) #When writing binary data to the target image file, you should write the entire content at once, rather than iterating through individual pixels

# Lambda Functions(Anonymous):Functions without name 

# Consider this function
def square(a):
     return a*a

print(square(5)) #25

# Here we need 2 lines of code for the simple function that we use only once in code.
# To optimize this, we can Anonymous/Lamba functions which simplifies the function into single line of code
# Syntax:
# lambda variable:expression
l=lambda a:a*a
print(l(5)) #25

# Always go for lambda function:
#     1)When you are going to call the function only once in the entire code
#     2)return expression is single line of code 
# Lambda functions can have 'n' number of arguments

# 3 important built-in function to work with lambda functions
    # 1)filter
    # 2)map
    # 3)reduce

# filter
# Filters each element of the iterable based on a specific condition
# To filter the even elements in a iterable without lambda functino
list_l=[2,4,5,6,9,10]
def Isevens(n):
     return n%2==0
Fil_list=list(filter(Isevens,list_l))
print(Fil_list) #[2, 4, 6, 10]

# Optimized using lambda function
lam_fil_list=list(filter(lambda n:n%2==0,list_l))
print(lam_fil_list)  #[2, 4, 6, 10]

# map
# iterates through the each element of list and applies function 
# without lamba function
def square(n):
     return n*n
map_list=list(map(square,list_l))
print(map_list) #[4, 16, 25, 36, 81, 100]
# with lambda function
lam_map_list=list(map(lambda n:n*n,list_l))
print(lam_map_list) #[4, 16, 25, 36, 81, 100]

# Reduce
# Reduce is part of functools module, we need to import it 
# Returns single value by applying cumulative operations on the iterables elements
# Without lambda function
def sum(a,b):
     return a+b
red_list=reduce(sum,list_l) #no need of list conversion here, as output will be a single value
print(red_list) #36
# with lambda function
lam_red_list=reduce(lambda a,b:a+b,list_l)
print(lam_red_list) #36









