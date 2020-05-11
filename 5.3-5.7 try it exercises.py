print("-- 5.3 Alien Colors #1 ")

alien_color = "yellow"

if alien_color is "green":
    points = 5
elif alien_color is "yellow":
    points = 3
elif alien_color is "red":
    points = 1
else:
    points = 0
print(f"You scored {points} points!")

#NO OUTPUT FAIL
print("\nThere will be no output for the example below.")
print("There is a else clause missing.")

alien_color= "blue"
if alien_color is "green":
    print("You scored 10 points")
print("\n----------------------------------------")
print("5.4 Alien colors #2")
alien_color = "green"
if alien_color is "green":
    points = 5
else:
    points = 10
print(f"You have earned {points} points!")

print("\nPractice with the ELSE clause")
alien_color = "green"
if alien_color is "blue":
    points = 5
else:
    points = 10
print(f"You have earned {points} points!")



print("\n------------------------------")
print("5.5 Alien Colors #3")

#Yellow Scenerio
alien_color = "yellow"

if alien_color is "green":
    print("GREEN!")
    points = 5
elif alien_color is "yellow":
    print("YELLOW")
    points = 10
elif alien_color is "red":
    print("RED")
    points = 15
else:
    print("NO COLORS")
    points = 0
print(f"You scored {points} points!")

#----------------------------------------------------------------
#Green Scenerio
alien_color = "green"

if alien_color is "green":
    print("GREEN!")
    points = 5
elif alien_color is "yellow":
    print("YELLOW")
    points = 10
elif alien_color is "red":
    print("RED")
    points = 15
else:
    print("NO COLORS")
    points = 0
print(f"You scored {points} points!")

#----------------------------------------------
#Red Scenerio
alien_color = "red"

if alien_color is "green":
    print("GREEN!")
    points = 5
elif alien_color is "yellow":
    print("YELLOW")
    points = 10
elif alien_color is "red":
    print("RED")
    points = 15
else:
    print("NO COLORS")
    points = 0
print(f"You scored {points} points!")

#-----------------------------------------
# None of the colors Scenerio
alien_color = "blue"

if alien_color is "green":
    print("GREEN!")
    points = 5
elif alien_color is "yellow":
    print("YELLOW")
    points = 10
elif alien_color is "red":
    print("RED")
    points = 15
else:
    print("None of the COLORS")
    points = 0
print(f"You scored {points} points!")

print("\n-------------------------------------")
print("5.6 Stages of Life")

age =66

if age < 2:
    stage = "baby"
elif 2 <= age < 4:
    stage= "toddler"
elif 4 <= age < 13:
    stage = "kid"
elif 13 <= age < 20:
    stage = "teenager"
elif 20 <= age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"
print(f"Based on your age you are in the {stage} stage of your life!")

print("\n-----------------------------------------")
print("5.7 Favorite Fruit")
fav_fruits = ["Mango", "Banana", "WaterMelon"]

print("These are the fruits that you like...")
if "Mango" in fav_fruits:
    print("You like Mangoes!")
if "Kiwi" in fav_fruits:
    print("You like Kiwis!")
if "Banana" in fav_fruits:
    print("You like Bananas!")
if "Apple" in fav_fruits:
    print("You like Apples")
if "WaterMelon" in fav_fruits:
    print("You like WaterMelons!")



