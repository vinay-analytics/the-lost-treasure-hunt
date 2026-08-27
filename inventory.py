class Inventory:

    def __init__(self):
        """
        Creates an empty inventory.
        """
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the inventory.
        """
        self.items.append(item)
        print(f"\n{item} has been added to your inventory!")

    def has_item(self, item):
        """
        Returns True if the item exists in the inventory.
        """
        return item in self.items

    def item_count(self):
        """
        Returns the number of collected items.
        """
        return len(self.items)

    def show_inventory(self):
        """
        Displays all collected items.
        """

        print("\n========== INVENTORY ==========")

        print(f"\nCollected Items: {self.item_count()}\n")

        if not self.items:
            print("Inventory is empty.")

        else:
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")

        print("\n===============================")