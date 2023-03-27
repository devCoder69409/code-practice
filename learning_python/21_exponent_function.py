#how to build an exponent function
#take a certain number and raise it to a specific power

# print(2**3) -simple sample 

def raise_to_power(base_num, pow_num): #will use this to multiply base_num by itself as many time as pow_num specifies
    result = 1 #result variable is where we store the actual result of doing the math
    for index in range(pow_num): #range will range us through a collection of numbers. when you put pow_num it will loop thru that.
        result = result * base_num
    return result

print(raise_to_power(2, 3))