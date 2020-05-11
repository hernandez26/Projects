# 3.4 guest list exercise
partylist =[ 'my Wifey','mom','dad','jose','mela', 'natalie', 'Rudy','AJ','Joshua']
partymessage = f"If I had a part I would invite the following people {partylist}"
print(partymessage)
for x in partylist:
    (
    print(f" Hi {x} you are invited to my party")
    )

print("---------------------------------------------------------------------------------------")
# 3.5 CHANGING GUEST LIST Exercise
cantmake= partylist.pop(6)
print(f"{cantmake} will not be able to attend!")
partylist.insert(6,'RJ')
newpm = f"invites will be sent instead to the following people {partylist}"
print(newpm)

for x in partylist:
    print(f" Hola {x}! Please join us for a fiesta!")

print('---------------------------------------------------------------------------------------------')
# 3.6 MORE GUESTS exercise
print(" Hi GUYS! it turns out that I found a bigger table! I will be inviting a few more guests!")
partylist.insert(0, 'BABY VICTOR')
partylist.insert(4, 'BECCA')
partylist.append('ARIANA')
addonMessage= f"The following guests have been added to my guest list {partylist[0]}, {partylist[4]}, {partylist[-1]}"
print(addonMessage)
for x in partylist:
    print(f"Hi {x}! You are invited to my party in B-Ville!")

print('---------------------------------------------------------------------------------------------')
#3.7 Shrinking Guest List
print(partylist)

print("Hi guests! it actually turns out that I only have room for 2 guests")
for x in range(10):
    popped_g= partylist.pop(-1)
    popped_m= f"Hi {popped_g} we had to uninvite you to make room! You've been popped!"
    print(popped_m)
for x in partylist:
    print(f"Hi {x} you are still invited!!")

del partylist[1]
del partylist[0]

print(partylist)

print("THE END!!")