class Player:

    def __init__(self, name):
        self.name = name

        # Player stats
        self.health = 100
        self.max_health = 100

        self.score = 0
        self.inventory = []

        # Location system
        self.current_location = None


    # -------------------------
    # Location Management
    # -------------------------

    def move_to(self, location):

        self.current_location = location

        print(
            f"\n📍 You moved to {location.name}"
        )
    # -------------------------
    # Inventory Management
    # -------------------------

    def add_item(self, item):
        self.inventory.append(item)


    def show_inventory(self):

        if len(self.inventory) == 0:
            print("Inventory is empty.")

        else:
            print("\n🎒 Inventory:")

            for item in self.inventory:
                print(f"- {item}")


    # -------------------------
    # Health System
    # -------------------------

    def take_damage(self, damage):

        self.health -= damage

        if self.health < 0:
            self.health = 0


        print(f"\n⚠️ You lost {damage} health!")

        self.show_health()


    def heal(self, amount):

        self.health += amount


        if self.health > self.max_health:
            self.health = self.max_health


        print(f"\n🧪 You recovered {amount} health!")

        self.show_health()



    def show_health(self):

        print(f"❤️ Health: {self.health}/{self.max_health}")


    def is_alive(self):

        return self.health > 0



    # -------------------------
    # Score System
    # -------------------------

    def add_score(self, points):

        self.score += points

        print(f"⭐ +{points} Score")



    def remove_score(self, points):

        self.score -= points


        if self.score < 0:
            self.score = 0


        print(f"⭐ -{points} Score")



    def show_status(self):

        print("\n========== PLAYER STATUS ==========")

        print(f"👤 Name: {self.name}")

        print(f"❤️ Health: {self.health}/{self.max_health}")

        print(f"⭐ Score: {self.score}")

        print("===================================")