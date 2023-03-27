
def cube(num):
    return num*num*num #return statement makes the function actually work and print out
    #print("code") #won't print because function ends after return statement.
    #you can not put any code after return statement. it won't get printed out.
    #basically as soon as the return keyword is used it breaks us out of function

print(cube(3))
print(cube(4))


result = cube(5) #result will store the value that gets returned executing the number
print(result)