#comparison operators 
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equals to
# != not equals to

#below function takes 3 parameters

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #boolean value and boolean value 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
print(max_num(3, 40, 5))
print(max_num(300, 40, 5))

#you can compare different datatypes such as strings, integers, booleans etc