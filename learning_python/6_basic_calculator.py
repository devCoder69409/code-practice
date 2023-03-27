#by default input is converted to string
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

#result = int(num1) + int(num2)
#in order to convert the input from user into numbers we can do that by making them integers using int() function

#print(result) #throws an error if the user puts a decimal number.

result = float(num1) + float(num2) #float lets you put decimal numbers too.
print(result)

