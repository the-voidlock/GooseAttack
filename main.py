import random


class _Goose:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


class ShieldGoose(_Goose):

    def __init__(self):

        super().__init__("Shield Goose", 10, 2)

    def attack(self, other):

        other.health -= self.damage
        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")

    def defend(self, damage):

        self.health -= damage

        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    def retaliate(self, damage):

        return damage / 2


class IceGoose(_Goose):

    def __init__(self):

        super().__init__("Ice Goose", 5, 2)

    def attack(self, other):

        other.health -= self.damage

        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")

    def defend(self, damage):

        self.health -= damage

        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    def freeze(self, other):

        if random.random() < 0.5:
            print(f"{other.name} has been frozen and cannot act this turn!")

            return True
        else:
            return False


class BasicGoose(_Goose):

    def __init__(self):

        super().__init__("Basic Goose", 1, 1)

    def attack(self, other):

        other.health -= self.damage

        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")


class CrippledGoose(_Goose):

    def __init__(self):

        super().__init__("Crippled Goose", 10, 1)

    def attack(self, other):

        other.health -= self.damage

        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")

    def defend(self, damage):

        self.health -= damage * 0.6

        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")


class FireGoose(_Goose):

    def __init__(self):

        super().__init__("Fire Goose", 10, 4)

    def attack(self, other):

        other.health -= self.damage

        if random.random() < 0.2:
            other.health -= 3
            print(f"{other.name} has been hit with a critical strike!")
        if other.health <= 0:
            print(f"{other.name} has been defeated!")

        else:
            print(f"{other.name} has {other.health} health remaining.")


class MedicGoose(_Goose):

    def __init__(self):
        super().__init__("Medic Goose", 5, 0)

    def heal(self, goose):
        goose.health += goose.health * 0.1

        print(f"{goose.name} has been healed for {goose.health * 0.1} health.")


class BombShelterGoose(_Goose):

    def __init__(self):
        super().__init__("Bomb Shelter Goose", 0, 0)

    def protect(self, goose):
        print(f"{goose.name} has been protected from damage for 1 turn.")


class RichGoose(_Goose):

    def __init__(self):
        super().__init__("Rich Goose", 15, 1)

    def steal(self, goose):
        print(f"{goose.name} has been stolen!")


class StormGoose(_Goose):

    def __init__(self):
        super().__init__("Storm Goose", 20, 0)

    def attack(self, other):
        if random.random() < 0.05:
            print(f"{other.name} has been instantly killed!")

            other.health = 0
        else:
            print(f"{other.name} has {other.health} health remaining.")


class ThermonuclearGoose(_Goose):

    def __init__(self):

        super().__init__("Thermonuclear Goose", 1, 4)

    def attack(self, other):

        other.health -= self.damage

        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")

    def thermonuclear(self):

        for goose in game.geese:
            if goose != self:
                goose.health -= 999

        print(f"{goose.name} has been hit with a thermonuclear blast!")


class CorruptedGoose(_Goose):

    def __init__(self):

        super().__init__("Corrupted Goose", 20, 2)

    def attack(self, other):

        other.health -= self.damage

        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name} has {other.health} health remaining.")

    def corrupt(self):

        self.damage += 2 * (self.health - self.health)

        print(f"{self.name} has been corrupted and now deals {self.damage} damage.")


class Game:

    def __init__(self):
        self.geese = [ShieldGoose(), IceGoose(), BasicGoose(), CrippledGoose(), FireGoose(), MedicGoose(),
                      BombShelterGoose(), RichGoose(), StormGoose(), ThermonuclearGoose(), CorruptedGoose()]

        self.deck = []
        self.hand = []


def draw(self):
    if len(self.deck) > 0:
        goose = random.choices(self.deck, weights=[0.5, 0.3, 0.1, 0.05, 0.03, 0.02])[0]


        self.hand.append(goose)
        self.deck.remove(goose)
        print(f"You have drawn a {goose.name}!")
    else:
        print("The deck is empty!")


def discard(self, goose):
    if goose in self.hand:
        self.hand.remove(goose)


        self.deck.append(goose)
        print(f"You have discarded a {goose.name}!")
    else:
        print(f"You do not have a {goose.name} in your hand!")

game = Game()
while True:
    print("1. Draw a goose")
    print("2. Discard a goose")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        game.draw()
    elif choice == "2":
        print("1. Shield Goose")
        print("2. Ice Goose")
        print("3. Basic Goose")
        print("4. Crippled Goose")
        print("5. Fire Goose")
        print("6. Medic Goose")
        print("7. Bomb Shelter Goose")
        print("8. Rich Goose")
        print("9. Storm Goose")
        print("10. Thermonuclear Goose")
        print("11. Corrupted Goose")
        goose_choice = input("Enter the number of the goose you want to discard: ")
        goose = game.geese[int(goose_choice) - 1]
        game.discard(goose)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
