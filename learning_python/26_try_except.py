
# handling errors, and do things when they occur.

# number = int(input("Enter a number: "))
# print(number)

#if the user puts anything other than a number, program throws an error. 

"""
Enter a number: asdasd
Traceback (most recent call last):
  File "/Users/emrenallar/Projects/learning_python/26_try_except.py", line 4, in <module>
    number = int(input("Enter a number: "))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'asdasd'
"""

#try/except is able to catch errors, and instead of throwing an error, you can put out a message for an invalid input. 


# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid input!")

# this helps us to protect our program. 
# we can not have something simple as invalid input. so try/except is great to use to eliminate these errors.

# value2 = 10/0 #this would normally throw a ZeroDivisionError:

try:
    number = int(input("Enter a number: ")) 
    print(number) 
#so you can use the error types in except to eliminate these errors from your program.
except ZeroDivisionError:
    print("Divided by zero.")
except ValueError: #using value error, we put a message out instead of a whole error. 
    print("Invalid input!")



try:
    value = 10/0
    number2 = int(input("Enter a number: ")) 
    print(number2) 
#so you can use the error types in except to eliminate these errors from your program.
except ZeroDivisionError as err: # we can actually store this error as an "err" variable. 
    print(err) # it will basically print out the error that we put in. 
except ValueError:
    print("Invalid input!") 
