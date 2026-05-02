


# Reverse a number
#===================


def reverse_number(n):

    if type(n) != int:
        print("Please enter a valid data type!")
        return

    num = n
    new_num = 0

    while num :
        digit = num%10
        new_num = new_num*10 + digit
        num = num // 10
    
    return new_num


print(reverse_number("deepanshu"))






# reverse a string
#====================

# 🔹 Method 1: Using Slicing (Most Recommended)
#-----------------------------------------------
def reverse_string(s):
    return s[::-1]

print(reverse_string("deepanshu"))



#🔹 Method 2: Using Loop (Manual Logic)
#----------------------------------------

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("deepanshu"))






#✅ 3️⃣ Palindrome Check
#=========================

def is_palindrome(s):
    return s == s[::-1]


def is_palindrome_number(n):
    return n == reverse_number(n)






# ✅ 4️⃣ Fibonacci Series
#==========================

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b





#✅ 5️⃣ Prime Number Check
#==========================

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True





#✅ 6️⃣ Remove Duplicates from List
#===================================

def remove_duplicates(lst):
    return list(set(lst))


def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result






# ✅ 7️⃣ Find Second Largest Element
#====================================

def second_largest(lst):
     
     second = float('-inf')
     first = lst[0]

     for i in range(1, len(lst)):
         
         if lst[i] > first:
             second = first
             first = lst[i]
         
         elif lst[i] > second and lst[i] != first:
             second = lst[i]

     return second





# ✅ 8️⃣ Count Frequency of Characters
#======================================

def char_frequency(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    return freq





# ✅ 9️⃣ Swap Two Numbers Without Third Variable
#===============================================

a = 5
b = 10

a, b = b, a





# ✅ 🔟 Find Factorial
#========================

def factorial(n):
    if n < 0:
        return "Not defined"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

