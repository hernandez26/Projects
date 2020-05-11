# practice looping through dictionary
user_0 = {
    'username': 'enfermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for x, y in user_0.items():
    print(f"\nKey: {x}")
    print(f"Value: {y}")
print("---------------------------------------------------")

#more looping through dictionary practice
fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'java'
    }
for name, language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.upper()}!")

print("--------------------------------------------------------------")
#Looping through all the keys in a Dictionary
for name in fav_languages.keys():
    print(name.upper())
# keys() is the default behavior
for x in fav_languages:
    print(x.title())

print('---------------------------------------------------------------------')

fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'java'
    }
friends = ['phil','sarah']

for name in fav_languages.keys():
    name2 = name.title()
    print(f"Hi {name2}!")

    if name in friends:
        lang = fav_languages[name].title()
        print(f"\t{name2}, I see you love {lang}!")
print('-------------------------------------------------------')
fave_goats ={
    'Juan': 'Lebron',
    'Rudy': 'Jordan',
    'Josue': 'Dwade',
    'Junior': 'Kobe',
    'Bryan': 'Durant',
    }

if 'danny' not in fave_goats.keys():
    print("Danny, please take our poll!")

print('--------------------------------------------------------')
#looping through a Dictionary's keys in a particular order!

fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'java'
    }
for x in sorted(fav_languages.keys()):
    print(f"{x.title()}, thank you for taking the poll!")


print('-----------------------------------------------------')
#Looping through all of the values in a dictionary!
fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'java',
    }
print("These are the languages that were mentioned:")
for x in fav_languages.values():
    lengua= x.upper()
    print(f"\t{lengua}")

print('-------------------------------------------------------')
#Using a set to get rid of duplicates
fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages were mentioned:")
for language in set(fav_languages.values()):
    print(f"{language.title()}")
