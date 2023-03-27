#loop thru different arrays
#loop thru letters inside a string
#loop thru numbers etc.
#we can use the for loops to loop thru essentially any collection that we have.

for letter in "Donkey Academy": #means: for every letter inside of "Donkey Academy" I want to do something
    print(letter) #this will basically print out each letter of "Donkey Academy" in every iteration of the loop on a new line. 

#with for loops, you define a variable, and every iteration of that loop it changes

print("") #intentionally left blank

friends = ["Jim", "Karen", "Kevin"]
for friend in friends: #for each friend inside of friends array, I want to print out a friend. friend = a variable. you can name it whatever you want
    print(friend)

print("") #intentionally left blank

for index in range(10): #this loop will print out every number in range 0 to 10 not including 10. 
    print(index)

print("") #intentionally left blank

for index in range(3, 10): #this will print from 3 upto 9 not including 10. 
    print(index)

friends = ["Jim", "Karen", "Kevin"]
#len(friends) would spit out number 3, because there are 3 elements inside of friends.
for index in range(len(friends)): #gives a range between 0 and number of friends. 
    print(friends[index]) #this will allows you to access each individual friend in the list.

print("") #intentionally left blank

friends = ["Jim", "Karen", "Kevin"]
for index in range(5): #put a different index number to see what happens
    if index == 0: #so that we know it is the first iteration of the loop
        print("First iteration")
    else:
        print("Not first") #this would be an example that maybe you want to do something on the first iteration of the loop
                            #and do something else on following loops. 

#don't be afraid to put more complex stuff inside for loops. it will make your programming better. 
