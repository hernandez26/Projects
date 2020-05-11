# Practice with NESTING
#A list of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('--------------------------------------------------')
# using range and for loop to create 30 aliens
aliens =[]

#make 30 green aliens
for x in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#Show the first five aliens
for x in aliens[:5]:
    print(x)
print('...')

#show how many alien have been created.
total= len(aliens)
print(f"The total number of aliens created are {total}")

print('-----------------------------------------------------')

# Changing characteristics of aliens
# empty list for aliens
aliens = []

# make 30 green aliens to start
for x in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for x in aliens[0:3]:
    for x in aliens[0:3]:
        if x['color'] is 'green':
            x['color'] = 'yellow'
            x['speed'] = 'medium'
            x['points'] = 10
        elif x['color'] == 'yellow':
            x['color'] = 'red'
            x['speed'] = 'fast'
            x['points'] = 15

# show the first 5 aliens
for x in aliens[:10]:
    print(x)

print('-----------------------------------------------------------------')

# STORE A LIST IN A DICTIONARY

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }

print(f"You ordered a {pizza['crust']} crust pizza," 
      " With the following toppings:")

for x in pizza['toppings']:
    print('\t' + x)

print('------------------------------------------------------------------')

fav_languages = {
    'jen': ['python','ruby'],
    'sarah': ['java'],
    'edward': ['php','xml'],
    'phil': ['C#','haskell'],
    }

for x, y in fav_languages.items():
    print(f"\n{x.title()}'s favorite languages are:")
    for z in y:
        print(f"\t {z.title()}")





