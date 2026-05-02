


# How to Read entire file or limited charactor
#------------------------------------------
print("# How to Read entire file or limited charactor")
f = open("sample.txt", 'r')
s = f.read(10) # print only 10 charactor
print(s)



# How to read line by line
#-------------------------
print("# How to read line by line")
f = open("sample.txt", 'r')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()


# Example

print("Example: How to read line by line!")
f = open("sample.txt", "r")

while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data, end='')
        
