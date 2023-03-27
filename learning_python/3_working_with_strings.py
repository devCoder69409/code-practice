print("Donkey\nAcademy") #separates the string into different lines
print("Donkey\"Academy") #\backslash lets you put quotation mark into the string
print("Donkey\Academy") #just prints backslash fine

phrase = "Donkey Academy"
print(phrase + " is cool.") #concatenation of strings with variables

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper()) #first uppers the string and then checks if it is upper - returns True
print(len(phrase)) #checks the length of the string
print(phrase[0]) #indexes 0 is the first charcter
print(phrase[3])
print(phrase.index("D")) #passing a parameter to find the index of the given character
print(phrase.index("Acad")) #checks where Academy word starts
print(phrase.replace("Donkey", "Horse")) #Replaces the existing string with the given one
print(phrase.index("z")) #throws an error as the substring doesn't exist.
