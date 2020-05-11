#3.8 Exercise- Seeing the World

places = ["punta cana","la romana","santo domingo", "azua","jarabacoa","puerto plata", "barahona"]
print("Original order")
print(places)
TSplaces = sorted(places)
print("Temporarily sorted order")
print(TSplaces)
print("original order again")
print(places)
RTSplaces = sorted(places,reverse=True)
print("temporarily reverse sorted order")
print(RTSplaces)
print("proof the order is still in original form")
print(places)
print("-------------------------------------------------------")
print("Using reverse order to reverse the list")
places.reverse()
print(places)
print("Using reverse the order to reverse the list once again and bring it back to its original form")
places.reverse()
print(places)
print("--------------------------------------------------------")
print("permanently sorting the list in alphabetical with sort()")
places.sort()
print(places)
print("permanently sorting the list in reverse alphabetical order using sort()")
places.sort(reverse=True)
print(places)

#3.9 Dinner guest length
guests= ["pita","baby victor", "becca","ariana"]
amountGuests= len(guests)
print(f"The total amount of guests is {amountGuests}")

#3.10 Every function
languages= ["english","spanish","french","polish","mandarin","italian", "japanese"]

print("\n\n-------------------------------------------------")
print("accessing the elements")
print(languages[1])

print("\n\n-------------------------------------------------")
print("changing the case of the elements")
print(languages[1].title())
print(languages[-1].upper())
print(languages[2].lower())

print("\n\n-------------------------------------------------")
print("using individual values from the list")
print(f"The languages that I am fluent in are {languages[0].upper()} and {languages[1].upper()}!")

print("\n\n-------------------------------------------------")
print("modifying items on a list")
languages[-2] = "german"
print(languages)

print("\n\n-------------------------------------------------")
print("adding items on a list")
languages.append("filipino")
print(languages)

print("\n\n-------------------------------------------------")
print("adding items using insert")
languages.insert(2,"korean")
print(languages)


print("\n\n-------------------------------------------------")
print("removing elements from a list del method")
del languages[-1]
print(languages)

print("\n\n-------------------------------------------------")
print("removing elements from list pop method")
poppedL= languages.pop(2)
print(languages)
print(poppedL)
print(f"The language that was popped was {poppedL}")

print("\n\n-------------------------------------------------")
print("removing an item by its value using remove")
languages.remove("polish")
print(languages)

print("\n\n-------------------------------------------------")
print("Temporarily sorting a list")
print(sorted(languages))
print("Temporarily sorting a list in reverse order")
print(sorted(languages,reverse=True))
print("proof that the order was only temporarily changed")
print(languages)

print("\n\n-------------------------------------------------")
print("printing the list in reverse using the reverse method")
languages.reverse()
print(languages)
print("once again changing the list to its original state using the reverse method again")
languages.reverse()
print(languages)

print("\n\n-------------------------------------------------")
print("finding the length of a list")
lOFlist = len(languages)
print(lOFlist)


print("\n\n-------------------------------------------------")
print("permanently sorting a list")
languages.sort()
print(languages)
print("permanently sorting a list in reverse order")
languages.sort(reverse=True)
print(languages)



