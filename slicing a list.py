cubbies03 = ['sammy', 'moises', 'aramis', 'corey', 'kerry', 'mark']
print(cubbies03[0:3])
print(cubbies03[2:6])
print(cubbies03[:6])
print(cubbies03[1:])
print(cubbies03[:])

print("\n")
print(cubbies03[2:])
print(cubbies03[-4:])

print(cubbies03[:2])
print(cubbies03[:-4])

# looping through a slice
teams= ["Cubs","Bears","Bulls","Fire","BlackHawks","Sox"]
print("Here are the first 3 teams in my list")
for x in teams[0:3]:
    print(x.upper())

print("Here are the rest of the teams!")
for T in teams[3:]:
    print(T.upper())




