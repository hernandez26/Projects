# Sorting a list Permanently with the sort Method

# printing in Alphabetical order
siblings= ["natalie","rudy","aj","joshua"]
siblings.sort()
print(siblings)

# printing in reverse alphabetical order
siblings.sort(reverse=True)
print(siblings)

#Temporarily sorting a list. "Sorted function"

stores = ["target", "sams", "jewel", "walmart", "ace", "home depot"]
print("Here is the original order of the list")
print(stores)

print("\nHere is the list sorted 'temporarily'")
print(sorted(stores))

print("\nHere is the list sorted backaward 'temporarily'")
print(sorted(stores, reverse =True))

print("\nHere is the list in its original order once again!")
print(stores)

#printing a list in REVERSE order ( doesnt sort reversed alphabetically. it just prints in reverse or original)

numbers= [1,2,3,4,5]
print("Before the reverse sort")
print(numbers)

numbers.reverse()
print("\nAfter the reverse sort")
print(numbers)

#Finding the length of a list

months= ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
length= len(months)
print(length)