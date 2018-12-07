def greet_world(greeting):
    print(greeting)
    greeting = greeting.lower()
    print(greeting)
    greeting = greeting.upper()
    print(greeting)
    greeting = greeting.title()
    print(greeting)
    greeting = greeting.swapcase()
    print(greeting)
    greeting = greeting.swapcase()
    print(greeting)

    greeting_array = [x for x in greeting]
    print(greeting_array)
    greeting_array.reverse()
    print(greeting_array)
    greeting = "".join(greeting_array)
    print(greeting)

    greeting_array = [x for x in greeting]
    print(greeting_array)
    greeting_array.reverse()
    print(greeting_array)
    greeting = "".join(greeting_array)
    print(greeting)

    greeting_length = len(greeting)
    print("Your greeting has " + str(greeting_length) + " characters")

greet_world("Humor is the universal solvent against the abrasive elements of life")