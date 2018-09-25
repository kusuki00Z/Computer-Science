import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Pokedex
# Shengnan Zhou
# ---------------------------------------
# This program is able to print out the
# pokedex, lookup pokemon by name or
# number, print the number of pokemon,
# and the total hit points of all
# pokemon depending on user's choice.
# ---------------------------------------

# Setup Class

class Pokemon:

    def __init__(self, name, number, combat_points, types):
        # Constructor
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.types = types


    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_combat_points(self):
        return self.combat_points

    def get_types(self):
        return self.types

    def __str__(self):
        if len(self.types) == 1:
            answer = "Number: " + str(self.number) + ", Name: " + self.name + ", CP: " + str(self.combat_points) + ", Types: " + self.types[0]
        else:
            answer = "Number: " + str(self.number) + ", Name: " + self.name + ", CP: " + str(self.combat_points) + ", Types: " + self.types[0] + " and " + self.types[1]

        return answer

# ---------------------------------------

# Print Menu

def print_menu():
    print()
    print("1. Print Pokedex")
    print("2. Lookup Pokemon by Name")
    print("3. Lookup Pokemon by Number")
    print("4. Print Number of Pokemon")
    print("5. Print Total Hit Points of All Pokemon")
    print("6. Quit")

# ---------------------------------------

# Choice 1, print pokedex

def print_pokedex(pokedex):

    print("\nThe Pokedex")
    print("-----------")

    for i in pokedex:
        print(i)

    print("-----------")
    print("End Pokedex\n")

# ---------------------------------------

# Choice 2, lookup by name

def lookup_by_name(pokedex, name):
    name_check = 0
    for i in pokedex:
        if name == i.get_name():
            print(i, "\n")
        else:
            name_check += 1

    if name_check > 29:
        print("No Pokemon named", name, "is in the Pokedex\n")

# ---------------------------------------

# Choice 3, lookup by number

def lookup_by_number(pokedex, number):
    num_check = 0
    for i in pokedex:
        if number == i.get_number():
            print(i, "\n")
        else:
            num_check += 1

    if num_check > 29:
        print("Pokemon number", number, "is not in the Pokedex\n")

# ---------------------------------------

# Choice 4, print the number of pokemons

def how_many_pokemon(pokedex):
    count = 0
    for i in pokedex:
        count += 1

    print("There are", count, "different Pokemon\n")

# ---------------------------------------

# Choice 5, print total combat points

def how_many_hit_points(pokedex):
    total_cp = 0
    for i in pokedex:
        total_cp += i.get_combat_points()

    print("The total number of combat points for all Pokemon in the Pokedex is", total_cp, "\n")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist.pop(0))           # number
        name = pokelist.pop(0)                  # name
        combat_points = int(pokelist.pop(0))    # hit points
        types = [pokelist.pop(0)]               # type
        if len(pokelist) == 1:
            types += [pokelist.pop(0)]          # optional second type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            how_many_pokemon(pokedex)
        elif choice == 5:
            how_many_hit_points(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
