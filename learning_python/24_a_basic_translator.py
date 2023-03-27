#Donkey Language
#vowels -> d
#-------------------
#dog -> ddg
#cat -> cdt
#on this program we are using a for loop in combination with if statements.

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #checking if the letter is inside of this string, then we know that it's a vowel.
            #if letter.lower() in "aeiou" can also be used- a little hack that we can use.
            if letter.isupper(): #checks if the letter is capital.
                translation = translation + "D" #if it is it prints D
            else:
                translation = translation + "d" #in the case of having a vowel, we are adding a d to translation.
        else:
            translation = translation + letter #in the case of NOT having a vowel, we are adding on whatever the letter was onto translation.
    return translation

print(translate(input("Enter a phrase: "))) #prints out translation of whatever the user enters in.