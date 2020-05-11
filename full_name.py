first_name = "jonathan"
last_name = "hernandez"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

assign = f"My name is {full_name.title()}, and this message is assigned to a variable named 'assign'."
print(assign)

formpract = "Hello {} {}. Nice to meet you!".format(first_name,last_name)
print(formpract)



django= "django"
jonH= " Jonathan"
Hjon= "Hernandez"

statement = f"my name is {jonH} {Hjon} and I want to learn how to make web apps with {django}"
print(statement)