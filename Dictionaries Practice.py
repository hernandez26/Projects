#Simple Dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print("--------------------------------------------------------------")

# accessing values in a dictionary
nombres= {'jman': 'Jonathan', 'pita': 'Maria', 'aj': "Anthony"}
print(nombres['aj'])
print(nombres['pita'])
print(nombres['jman'])
print("--------------------------------------------------------------")
alien_0 ={'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print("--------------------------------------------------------------")

#Adding new key-value pairs

alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("-------------------------------------------------------------------")
#Starting with an empty dictionary
alien_0={}

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

print('---------------------------------------------------------------------')
#Modifying Values in a Dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['points'])
print(alien_0['color'])

print(f" The alien color is {alien_0['color']} and the points won is {alien_0['points']} points!")
# Modify values

alien_0['color'] = "yellow"
alien_0['points'] = 3

print(f"The new alien color is {alien_0['color']} and the new points won is {alien_0['points']} points!")


alien_0= {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original X-Position: {alien_0['x_position']}")

# IF statement to determine how much alien has moved according to speed.

if alien_0['speed'] is 'slow':
    x_increment = 1
elif alien_0['speed'] is 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New X-Position: {alien_0['x_position']}")

print("---------------------------------------------------------------------------")
#Removing Key-Value Pairs
alien_0= {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print("---------------------------------------------------------------------------")
#Dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'java',
    'edward': 'ruby',
    'phil': 'c#',
    }

SarahLang = favorite_languages['sarah'].upper()
print(f"Sarah's favorite programming language is {SarahLang}!")

print("--------------------------------------------------------------------------")
#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
# this produce KeyError because it doesnt exist-> print(alien_0['puntos'])

point_value = alien_0.get('puntos', 'No point value assigned.')
point_value = alien_0.get('puntos') # another option. Will display "None"
color_value = alien_0.get('color', 'No point value assigned')
print(point_value)
print(color_value)



