#in simple terms: dictionary in python means key: value pairs. 
#the word will be the key
#the value will be the actual definition
#you can convert values using dictionaries
#you can not have duplicate keys, each key needs to be unique

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#accessing entries in dictionary
print(month_conversions["Nov"]) #referring to the key
# print(month_conversions["Hel"]) #this will throw a KeyError as "Hel" is not a key in dictionary
print(month_conversions.get("Dec")) #using get function actually specifies a default that you want to use if the given key is not found
print(month_conversions.get("Luv")) #it will print None as default
print(month_conversions.get("Luv", "Not a valid key")) #using get function, you can assign a value to an invalid key


#you can use numbers too with dictionaries as long as they are unique.
# month_conversions_in_numbers = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December",
# }

# print(month_conversions_in_numbers.get(1))
# print(month_conversions_in_numbers.get(13, "Not a valid key"))