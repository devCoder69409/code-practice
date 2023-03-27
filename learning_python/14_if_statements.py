
is_male = True
is_tall = True #Play around with conditions to see the outcome to better understand use of operators "or", "and".

print("Outcome of single statement is_male:")
if is_male:
    print("You are a male.") #prints when the condition is true as default.
else:
    print("You are not a male.") #prints when the condition is false.

print("")
print("Outcome of 'or' operator:")
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")

print("")
print("Outcome of 'and' operator:")
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall): #elif stands for "else if". this condition checks if it is male but not tall
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
else:
    print("You are not a male and not tall.")


#is_male_2 = False
#if is_male_2:
    #print("You are a male.") #this won't print anything as the condition is False.