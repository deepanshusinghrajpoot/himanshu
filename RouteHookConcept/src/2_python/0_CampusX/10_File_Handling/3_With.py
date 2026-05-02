


# Using Context Manager (With)
#==============================

# It's a good idea ro close a file after usage as it will free upp
# If we don not close it, garbage collector would close it
# with keyword close the file as soon as the usage is over



# write operation using with
#---------------------------

with open("sample.txt", "w") as f:
    f.write("Deepanshu Singh!")




# read operation using with
#--------------------------
    