#indentetion important.

# def say_hi():
#    print("Hello User") #you need to call the function for it to be printed

# print("top") #starts from top
# say_hi() #this actually prints the function #goes back to function and prints it.
# print("bottom")  #then goes to the next thing on the list


#USING PARAMETERS
def say_hi(name, age):
    print("Hello " + name + ", you are " + age + " years old.")
say_hi("Mike", "35") #recieving parameters
say_hi("Steve", "70")

def say_hi_2(name2, age2):
    print("Hello " + name2 + ", you are " + str(age2) + " years old.") #you need to convert the age parameter into string.
say_hi_2("Mikey", 35) #so that you can use integers too
say_hi_2("Stevo", 70)