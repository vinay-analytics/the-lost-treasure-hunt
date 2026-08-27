class Location:
    """
    Represents a place in the game world.
    """

    def __init__(
        self,
        name,
        description,
        puzzle=None,
        required_item=None
    ):
        """
        Creates a location.

        Parameters:
        ----------
        name : str
            Name of the location.

        description : str
            Description displayed when explored.

        puzzle : Puzzle | None
            Puzzle available at this location.

        required_item : str | None
            Item required to enter this location.
        """

        self.name = name
        self.description = description
        self.puzzle = puzzle

        # Connected locations
        self.connections = []

        # Required inventory item
        self.required_item = required_item

    def display_location(self):

        print(f"\n========== {self.name.upper()} ==========")

        print(self.description)

        if self.has_puzzle():

            if self.puzzle.is_completed():
                print("\nPuzzle Status : COMPLETED")
            else:
                print("\nPuzzle Status : AVAILABLE")

        print("=" * 45)

    def has_puzzle(self):

        return self.puzzle is not None

    def add_connection(self, location):

        self.connections.append(location)

    def show_connections(self):

        print("\nAvailable Paths")

        print("-" * 25)

        for index, location in enumerate(
            self.connections,
            start=1
        ):

            if location.required_item:

                print(
                    f"{index}. {location.name} "
                    f"(Requires: {location.required_item})"
                )

            else:

                print(
                    f"{index}. {location.name}"
                )

    def requires_item(self):

        return self.required_item is not None