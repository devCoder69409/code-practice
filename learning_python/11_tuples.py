#basically a structure where we can store different values. similar to a list.
#but key differences are: they are in double paranthesis 
#and tuples are immutable. cannot be changed or modified.


coordinates = (4, 5)
#coordinates[1] = 10 #throws an error. tuple does not support item assignment
print(coordinates[0])
print(coordinates[1])

coordinates2 = [(4, 5), (6, 7), (80, 34)] #list of tuples
print(coordinates2)
