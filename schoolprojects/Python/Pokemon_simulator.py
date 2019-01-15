# TIE-02100 Introduction to Programming
# Nimi: Elias Örmä, Opiskelijanumero: 266561
# Status: READY

# This dict is a global constant, that will be used to determine the
# effectiveness factor of the Pokémon attacks. The keys of this dict are
# Pokémon types. The values related to the keys are dicts, where the keys
# are attack types and values are the effect factors of the attacks.
# Example: a Ghost-type attack toward a Normal-type Pokémon causes 0.8* damage
# and a Fighting-type attack toward the same Pokémon causes 1.25* damage.
TYPES = {"Normal": {"Fighting": 1.25, "Ghost": 0.8},
         "Fighting": {"Flying": 1.25, "Psychic": 1.25, "Fairy": 1.25,
                      "Rock": 0.8, "Bug": 0.8, "Dark": 0.8},
         "Flying": {"Electric": 1.25, "Rock": 1.25, "Ice": 1.25, "Grass": 0.8,
                    "Bug": 0.8, "Fighting": 0.8, "Ground": 0.8},
         "Poison": {"Ground": 1.25, "Psychic": 1.25, "Fighting": 0.8,
                    "Bug": 0.8, "Poison": 0.8, "Grass": 0.8, "Fairy": 0.8},
         "Ground": {"Water": 1.25, "Grass": 1.25, "Ice": 1.25, "Poison": 0.8,
                    "Rock": 0.8, "Electric": 0.8},
         "Rock": {"Fighting": 1.25, "Ground": 1.25, "Steel": 1.25,
                  "Water": 1.25, "Grass": 1.25, "Normal": 0.8, "Flying": 0.8,
                  "Poison": 0.8, "Fire": 0.8},
         "Bug": {"Flying": 1.25, "Rock": 1.25, "Fire": 1.25, "Fighting": 0.8,
                 "Ground": 0.8, "Grass": 0.8},
         "Ghost": {"Ghost": 1.25, "Dark": 1.25, "Bug": 0.8, "Poison": 0.8,
                   "Normal": 0.8, "Fighting": 0.8},
         "Steel": {"Fighting": 1.25, "Ground": 1.25, "Fire": 1.25,
                   "Normal": 0.8, "Flying": 0.8, "Rock": 0.8, "Bug": 0.8,
                   "Steel": 0.8, "Grass": 0.8, "Psychic": 0.8, "Ice": 0.8,
                   "Dragon": 0.8, "Fairy": 0.8, "Poison": 0.8},
         "Fire": {"Ground": 1.25, "Rock": 1.25, "Water": 1.25, "Bug": 0.8,
                  "Steel": 0.8, "Fire": 0.8, "Ice": 0.8, "Fairy": 0.8},
         "Water": {"Grass": 1.25, "Electric": 1.25, "Steel": 0.8, "Fire": 0.8,
                   "Water": 0.8, "Ice": 0.8},
         "Grass": {"Flying": 1.25, "Poison": 1.25, "Bug": 1.25, "Fire": 1.25,
                   "Ice": 1.25, "Ground": 0.8, "Water": 0.8, "Grass": 0.8,
                   "Electric": 0.8},
         "Electric": {"Ground": 1.25, "Flying": 0.8, "Steel": 0.8,
                      "Electric": 0.8},
         "Psychic": {"Bug": 1.25, "Ghost": 1.25, "Dark": 1.25, "Fighting": 0.8,
                     "Psychic": 0.8},
         "Ice": {"Fighting": 1.25, "Rock": 1.25, "Steel": 1.25, "Fire": 1.25,
                 "Ice": 1.25},
         "Dragon": {"Ice": 1.25, "Dragon": 1.25, "Fairy": 1.25, "Fire": 0.8,
                    "Grass": 0.8, "Water": 0.8, "Electric": 0.8},
         "Dark": {"Fighting": 1.25, "Bug": 1.25, "Fairy": 1.25, "Ghost": 0.8,
                  "Psychic": 0.8},
         "Fairy": {"Poison": 1.25, "Steel": 1.25, "Fighting": 0.8, "Bug": 0.8,
                   "Dark": 0.8, "Dragon": 0.8}}


def factor(attack_type, pokemon_type):
    """
    Finds the effectiveness factor of an attack from the above defined
    datastructure.
    :param attack_type: String, type of the move used in attack
    :param pokemon_type: String, one of the defending Pokemons types
    :return: Returns the effectiveness factor of the attack
    """
    if pokemon_type in TYPES:

        if attack_type in TYPES[pokemon_type]:
            return TYPES[pokemon_type][attack_type]

    return 1


class Pokemon:
    """Implements one Pokémon that has species, types, hit points and moves."""

    def __init__(self, species, types):
        """
        Constructor of the class.
        :param species: String
        :param types: List
        """

        self.__species = species.capitalize()
        self.__types = types

        self.__max_hp = 100
        self.__hp = self.__max_hp

        # __moves = dict:list
        self.__moves = {}


    def damage(self, hp):
        """
        Hit points are reduced by the amount of parameter hp, but not under 0.
        :param hp: int
        """

        if hp >= self.__hp:
            damage = self.__hp
            self.__hp = 0
            print(self.__species, "fainted!")

        else:
            self.__hp -= hp
            damage = hp

        print("{:s} lost {:d} hp.".format(self.__species, damage))

    def info(self):
        """Prints pokemons species,hp,types"""

        print(self.__species,", ", self.__hp, "hp, Types: ",", ".join(self.__types), sep="")

    def move_info(self):
        """Prints pokemons moves in sorted order"""

        for move in sorted(self.__moves):
            move_name = move
            move_power = self.__moves[move][0]
            move_type = self.__moves[move][1]
            print("  - {}, {}, {}" .format(move_name, move_power, move_type))

    def add_move(self, name, power, move_type):
        """Adds move to specific pokemons moves. and RETURNS TRUE
        If the pokemon already has 2 moves it doesent add the move and RETURNS FALSE"""

        name = name.title()
        power = int(power)

        if len(self.__moves) < 2:
            power_type = []
            power_type.append(power)
            power_type.append(move_type)
            self.__moves[name] = power_type
            return True

        else:
            return False

    def attack(self, move, defender):
        """Takes 2 parameters: move and defenderclass
        It uses other methods and functions to calculate the damage.
        This function prints all the action caused by attack"""
        if self.__hp == 0:
            print("Pokemon has fainted and can't attack.")

        elif move not in self.__moves:
            print("Attack named", move, "was not found.")
        else:
            move_used = self.__moves[move]
            attack_power = move_used[0]
            attack_type = move_used[1]
            effectiveness_factor = 1
            if len(defender.__types) > 1:
                for def_type in defender.__types:
                    effectiveness_factor *= factor(attack_type, def_type)
            else:
                effectiveness_factor = factor(attack_type, defender.__types[0])

            attack_damage = int(attack_power * effectiveness_factor)

            print(self.__species, " used ", move, ".", sep="")

            if effectiveness_factor < 1:
                print("It's not very effective.")

            elif effectiveness_factor > 1:
                print("It's super effective!")

            defender.damage(attack_damage)

    def heal(self, amount):
        """Adds the wanted amount of hp, but hp can't be over the maximum hp of
        the pokemon"""
        if amount > 0:
            if amount + self.__hp <= self.__max_hp:
                self.__hp += amount
                print(self.__species, "was healed for", amount, "hp.")
            else:
                healed = self.__max_hp - self.__hp
                self.__hp = self.__max_hp
                print(self.__species, "was healed for", healed, "hp.")
        else:
            print(self.__species, "was healed for 0 hp.")


    def get_hp(self):
        return self.__hp

    def get_species(self):
        return self.__species

    def __lt__(self, other):
        return self.__hp < other.__hp



def read_file(pokemonfile):
    """This function reads the ordered infofile if there is one.
        Funktion prints error message and RETURNS an empty it if there is any
        errors reading the file. Else funktion
        RETURNS dict with the pokemons from the file"""
    filedict = {}
    try:
        file = open(pokemonfile, "r")
        for i in file:
            info_list = i.rstrip().split(";")
            species = info_list[0]
            types = info_list[1]; moves = info_list[2:] ; types = types.split(",")

            for i in types:
                if i.title() in TYPES:
                    continue
                else:
                    raise OSError

            type_list = []
            for i in types:
                type_list.append(i)

            object = Pokemon(species, type_list)
            for i in moves:
                name, power, type = i.split(",")

                if type.title() in TYPES:
                    power = int(power)
                    object.add_move(name, power, type)
                else:
                    raise OSError

            filedict[species] = object

        file.close()

        return filedict

    except OSError:
        print("Error: file cannot be read.")
        return {}



def main():

    pokedict ={}
    pokemonfile = input("Pokemon file: ")
    if pokemonfile != "":
        file_data = read_file(pokemonfile)
        if file_data != {}:
            pokedict = file_data
        else:
            raise SystemExit

    while True:
        command = input("> ")
        command = command.upper()

        if command == "NP":
            check = True # Checks if the pokemon is going to be added in to pokedict
            species = input("Enter a new species: ")

            if not species in pokedict:
                types = input("Enter types separated by comma: ")
                types = types.split(",")

                for i in types:
                    if i.title() in TYPES:
                        continue

                    else:
                        print("Error: unknown type.")
                        check = False

                if check:
                    type_list = []

                    for i in types:
                        type_list.append(i)
                    object = Pokemon(species, type_list)
                    pokedict[species] = object
            else:
                print("Error: Pokemon", species, "already exists.")

        elif command == "L":
            for i in sorted(pokedict):
                pokedict[i].info()
                pokedict[i].move_info()


        elif command == "R":  # Deletes existing pokemon

            to_remove = input("Enter species to remove: ")
            try:
                del pokedict[to_remove.title()]

            except KeyError:
                print("Error: Pokemon was not found.")

        elif command == "NM":
            atk_species = input("Enter species: ")
            if not atk_species in pokedict:  # checks if pokemon is in pokedict
                print("Error: Pokemon was not found.")

            else: #Checks all the input data if they are good it adds move trough classmethod.
                atk = input("Enter a move in the form name,power,type: ")

                try:
                    name, power, type = atk.split(",")

                    if type.title() in TYPES:

                        power = int(power)
                        if pokedict[atk_species].add_move(name,power,type):
                            print("New move added.")

                        else:
                            raise TypeError
                    else:
                        raise TypeError
                except TypeError:
                    print("Error: incorrect input or too many moves.")
                except ValueError:
                    print("Error: incorrect input or too many moves.")


        elif command == "A": #Checks if Attacker,Defender and Attackers move exist and uses classmethod.
            attacker = input("Attacker: ")
            if not attacker in pokedict:
                print("Error: Pokemon was not found.")
            else:
                defender = input("Defender: ")
                if not defender in pokedict:
                    print("Error: Pokemon was not found.")
                else:
                    attacker = pokedict[attacker]
                    defender = pokedict[defender]
                    move = input("Attack move: ")
                    attacker.attack(move,defender)

        elif command == "UP": #Heals pokemon trough method
            species = input("Enter species: ")

            if species not in pokedict:
                print("Error: Pokemon was not found.")
            else:
                try:
                    amount = int(input("Enter the amount of healing: "))
                    pokedict[species].heal(amount)

                except ValueError:
                    print("Error: invalid amount of healing.")

        elif command == "T":
            """ This part lists pokemons based on amount of hp-left."""
            hp_list = []
            for i in sorted(pokedict): #uses method __lt__ to sort.
                hp_list.append(pokedict[i])

            for i in sorted(hp_list, reverse=True):
                hp = i.get_hp()
                species = i.get_species()
                print("{:>3} hp: {}".format(hp, species))

        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NP (New Pokemon)")
            print("L (List)")
            print("R (Remove)")
            print("NM (New Move)")
            print("A (Attack)")
            print("UP (Use Potion)")
            print("T (Top list)")
            print("Q (Quit)")


main()

