
employee_file = open("28_writing_to_files.txt", "a") # "a" adds text to the end of the file
employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service") #\n is a newline character to make sure the new input is in a newline on your file. 

employee_file.close()

# employee_file = open("28_writing_to_files.txt", "w") # "w" overwrites the entire file. 
# employee_file.write("\nKelly - Customer Service") #because of "w" this input will replace everything in the file. 

# employee_file.close()

employee_file = open("28_writing_to_files_1.txt", "w") # by adjusting the name of the file, we can write the new information on a newly created file. 
employee_file.write("\nKelly - Customer Service") 

employee_file.close()

#you can also use different extensions such as one for HTML: 
# employee_file = open("index.html", "w")
# employee_file.write("<p>This is HTML</p>") 

# employee_file.close()
