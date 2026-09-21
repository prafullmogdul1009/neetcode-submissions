class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name= name
        self.power= power
        self.health = health
        print( self.name)
        print( self.power)
        print(self.health)
        pass


# TODO: Create Superhero instances
i1 = SuperHero("Batman",  "Intelligence", 100)
i2 = SuperHero("Superman",  "Strength", 150)


# TODO: Print out the attributes of each superhero
