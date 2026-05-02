

"""

✅ Exception Handling in Python (Easy & Interview Friendly)

Exception
An exception is a runtime error that interrupts the normal flow of a program.


                        
try
Used to write code that may cause an error.

except
Used to catch and handle the error.

else
Runs only if no error occurs.

finally
Runs always, whether an error occurs or not.


"""


# let's create a file
with open("sample.txt", "w") as f:
    f.write("Hellow world!")


# catching specific exception 
#............................

try:
    with open("sample1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print("sorry file not found!", e.with_traceback)

# sorry file not found! <built-in method with_traceback of FileNotFoundError object at 0x000001FD4AA50940>


# handle exception
#.................

try:
    with open("sample.txt", "r") as f:
        m = 3
        print(f.read())
        print(m)
        print(5/2)
        L = [1, 2, 3, 4]
       # print(L[100])

except FileNotFoundError:
    print("File is not found!")

except NameError:
    print("Variable is not found!")

except ZeroDivisionError:
    print("Division by zero not allow!")

except Exception as e:
    print(e)

else:
    print("Finally we are not found any error!")

finally:
    print("Ye to print hoga hi!")



# Hellow world!
# 3
# 2.5
# Finally we are not found any error!

