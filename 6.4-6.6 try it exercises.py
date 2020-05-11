# 6-44 Glossary part 2
glossary = {
    'print': '-print():\n\tThe print function outputs the code you have written in the program.',
    'f-strings': '-f strings:\n\tF Strings allow us to use variable names inside of a print function.',
    'ifs': '-IF statements:\n\tIF Statements are conditional statement that we can use in our programs.',
    'for': '-For Loops:\n\tFor Loops allow us to repeat actions several time while writing it once.',
    'list': '-Lists:\n\tLists are containers where we can store data and later manipulate them.',
    'Dictionary': '-Dictionary: \n\tDictionaries hold Key Values pairs that are associated with each other.',
    'set':'-Set:\n\tSets are similar to lists but delete duplicates within the list',
    'tuple': '-Tuple:\n\tTuples are similar to list but are immutable one they are created',
    'sorted': '-Sorted():\n\tThe sorted function sorts a list in alphabetical order.',
    }
for x in glossary.values():
    print(x.upper())

print('-----------------------------------------------------------')
#6-5 Rivers
rivers = {'nile': 'egypt', 'amazon': 'Brazil', 'Mississippi': 'usa', 'yellow': 'China',}

for name in rivers.keys():
    country = rivers[name].title()
    print(f"The {name.title()} river is located in {country}!")

print('-----------------------------------------------------------------')
# 6-6 polling
fav_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'phil': 'java'
    }
people = ['jen','yoel','pablo','sarah','james','phil','dustin','edward']

for x in people:
    if x in fav_languages:
        print(f"\nDear {x.title()}, thank you for taking the poll!")
    else:
        print(f"\nHi {x.title()} we would appreciate if you took the poll!")
