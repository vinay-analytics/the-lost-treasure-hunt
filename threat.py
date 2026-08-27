"""
threat.py

Handles traps and threats that damage the player
during challenge puzzles.
"""


class Threat:
    """
    Represents a trap or environmental threat.
    """

    def __init__(self, name, damage, message):
        """
        Parameters:
            name (str): Name of the threat.
            damage (int): Health damage.
            message (str): Description shown to the player.
        """

        self.name = name
        self.damage = damage
        self.message = message


    def activate(self, player):
        """
        Activates the threat and damages the player.
        """

        print("\n===================================")
        print(f"⚠️  THREAT: {self.name}")
        print("===================================")

        print(self.message)

        player.take_damage(self.damage)

        print("===================================\n")