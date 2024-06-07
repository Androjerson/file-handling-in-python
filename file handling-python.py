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
        tgt_img.write(image)



