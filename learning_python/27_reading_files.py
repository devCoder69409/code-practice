
#"r" stands as read "w" means write.
# "a" means append: you can add information to the file. 
# #"r+" reading and writing. 

# employee_file = open("27_reading_files.txt", "r")
# print(employee_file.read())
# print(employee_file.readline()) # readsout first line.
# print(employee_file.readline()) # reads out second line and so on.
# print(employee_file.readlines()) # reads out all the lines as an array.

# print(employee_file.readable()) #returns a boolean to show if the file is actually readable or not. 


# employee_file.close() # whenever you open a file, it is ideal to close a file when you are done with it. 

employee_file = open("27_reading_files.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
