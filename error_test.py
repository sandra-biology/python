def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

# get name and greeting, send to make_greeting 
print(make_greeting(get_name(), get_greeting()))

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry