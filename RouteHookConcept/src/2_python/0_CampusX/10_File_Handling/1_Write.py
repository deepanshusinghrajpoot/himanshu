
# Writing to a file
#==================
import os



# case 1 - if the file is not persent
#------------------------------------

f = open('sample.txt', 'w')
f.write('Hellow Deepanshu You now read file handling!')
f.write("\nHow are you!")
f.close()


print(os.getcwd()) 
# f.write("hahahahah") # give error


# Case 2 - if the file is already present we want erase existing content write new content
#-----------------------------------------------------------------------------------------

f = open("sample.txt", "w")
f.write("salman khan")
f.close()

# Note: When you perform write operation on existing file then its content erase and write new content



# Case 3 - if the file is already present we want without erase existing content write new content
#-------------------------------------------------------------------------------------------------

f = open("sample.txt", "a")
f.write("\nI am fine!")
f.close()



# Case 3 - How to write multiple line
#------------------------------------

L = ["hellow\n", "hi\n", "how are you\n", "I am fine!"]

f = open("sample.txt", "a")
f.writelines(L)
f.close()
