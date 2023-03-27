lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Toby"]
friends.append("Creed") #adds the value at the end of the list
friends.insert(1, "Kelly") #inserts the value at index position 1
friends.remove("Jim")
#friends.clear() #clears the friends list completely
friends.pop() #removes the last element from the list
#friends.extend(lucky_numbers) #puts two lists together
#print(friends)

print(friends.index("Kevin")) #prints out the index of Kevin
print(friends.index("Oscar")) #prints index of Oscar
print(friends.count("Jim")) #prints out how many times the value used in the list
#print(friends.index("Mike")) #throws an error as Mike is not in the list
friends.sort()
print(friends)

lucky_numbers.sort() #sorts in ascending order
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers) #reverses the order of the list

friends2 = friends.copy()
print(friends2) #copies the friends list