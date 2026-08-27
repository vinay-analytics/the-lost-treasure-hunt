"""
THE LOST TREASURE HUNT
game.py v0.82 - Clean Colorama CLI
"""

from player import Player
from location import Location
from puzzle import Puzzle
from timer import GameTimer
from threat import Threat

import time
import random
import os
import shutil

from colorama import Fore, Style, init

init(autoreset=True)

class Game:

    UI_MIN_WIDTH = 90

    # =========================================
    # CLEAN CLI UI
    # =========================================

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_ui_width(self):
        terminal_width = shutil.get_terminal_size(
            fallback=(120, 30)
        ).columns

        # Leave a safety margin so the two dashboard panels never wrap
        # onto the next terminal line.
        usable_width = terminal_width - 8

        return max(self.UI_MIN_WIDTH, usable_width)

    def box(self, title, lines=None, color=Fore.WHITE):
        width = self.get_ui_width()
        border = "─" * (width - 2)

        print(color + "┌" + border + "┐" + Style.RESET_ALL)
        print(
            color
            + "│"
            + f" {title} ".center(width - 2)
            + "│"
            + Style.RESET_ALL
        )

        if lines:
            print(color + "├" + border + "┤" + Style.RESET_ALL)

            content_width = width - 4

            for item in lines:
                for part in self.wrap_text(item, content_width):
                    part = part[:content_width]
                    print(
                        color
                        + "│ "
                        + part.ljust(content_width)
                        + " │"
                        + Style.RESET_ALL
                    )

        print(color + "└" + border + "┘" + Style.RESET_ALL)

    def menu_box(self, title, rows, color=Fore.WHITE):
        """Print a fixed two-column menu without collapsing alignment spaces."""
        width = self.get_ui_width()
        inner = width - 2
        content_width = width - 4

        print(color + "┌" + "─" * inner + "┐" + Style.RESET_ALL)
        print(
            color
            + "│"
            + f" {title} ".center(inner)
            + "│"
            + Style.RESET_ALL
        )
        print(color + "├" + "─" * inner + "┤" + Style.RESET_ALL)

        for left, right in rows:
            column_width = content_width // 2
            line = f"{left:<{column_width}}{right}"
            line = line[:content_width]

            print(
                color
                + "│ "
                + line.ljust(content_width)
                + " │"
                + Style.RESET_ALL
            )

        print(color + "└" + "─" * inner + "┘" + Style.RESET_ALL)

    def map_lines(self):
        """Return a clean, centered vertical treasure route."""

        total_width = self.get_ui_width()
        gap = 4
        panel_width = max(38, (total_width - gap) // 2)
        content_width = panel_width - 4

        cave_name = (
            "Dark Cave"
            if getattr(self, "cave_lit", False)
            else "????????????????????"
        )

        locations = [
            "Treasure Room",
            "Ancient Library",
            cave_name,
            "Abandoned Cabin",
            "Ancient Forest"
        ]

        lines = []

        for index, location in enumerate(locations):
            lines.append(location.center(content_width))

            if index < len(locations) - 1:
                lines.append("│".center(content_width))

        return lines

    def dashboard(self):
        """Render Player + Actions on the left and Map on the right."""

        self.clear_screen()

        if not self.player.is_alive():
            self.game_over()
            return

        total_width = self.get_ui_width()

        # Reserve a small gap between the two panels.
        gap = 4

        # Both panels use exactly the same width.
        panel_width = max(38, (total_width - gap) // 2)

        def panel(title, rows, color=Fore.WHITE):
            inner = panel_width - 2
            content_width = panel_width - 4

            result = [
                "┌" + "─" * inner + "┐",
                "│" + f" {title} ".center(inner) + "│",
                "├" + "─" * inner + "┤"
            ]

            for row in rows:
                row = str(row)

                # Keep every row strictly inside the panel.
                if len(row) > content_width:
                    row = row[:content_width]

                result.append(
                    "│ " + row.ljust(content_width) + " │"
                )

            result.append("└" + "─" * inner + "┘")

            return result, color

        player_rows = [
            f"Explorer : {self.player.name}",
            f"Location : {self.current_location.name}",
            f"Health   : {self.player.health}/{self.player.max_health}",
            f"Score    : {self.player.score}",
            f"Items    : {len(self.player.inventory)}"
        ]

        action_rows = [
            "1  Explore Location",
            "2  Travel",
            "3  Inventory",
            "4  Exit"
        ]

        # The map is always present on the right.
        map_rows = self.map_lines()

        player_panel, player_color = panel(
            "PLAYER",
            player_rows,
            Fore.CYAN
        )

        action_panel, action_color = panel(
            "ACTIONS",
            action_rows,
            Fore.WHITE
        )

        map_panel, map_color = panel(
            "TREASURE MAP",
            map_rows,
            Fore.CYAN
        )

        # Left side = Player + Actions only.
        left = []
        left.extend(player_panel)
        left.append(" " * panel_width)
        left.extend(action_panel)

        # Right side = Map only.
        right = map_panel

        # Make both columns the same height.
        height = max(len(left), len(right))

        left += [" " * panel_width] * (height - len(left))
        right += [" " * panel_width] * (height - len(right))

        # Print each row as one controlled terminal line.
        for i in range(height):

            if i < len(player_panel):
                left_color = player_color
            else:
                left_color = action_color

            print(
                left_color
                + left[i]
                + Style.RESET_ALL
                + " " * gap
                + map_color
                + right[i]
                + Style.RESET_ALL
            )

        print()

    def wrap_text(self, text, width):
        words = str(text).strip().split()

        if not words:
            return [""]

        result = []
        current = words[0]

        for word in words[1:]:
            if len(current) + 1 + len(word) <= width:
                current += " " + word
            else:
                result.append(current)
                current = word

        result.append(current)
        return result

    def success(self, text):
        print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)

    def error(self, text):
        print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

    def warning(self, text):
        print(Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL)

    def info(self, text):
        print(Fore.CYAN + text + Style.RESET_ALL)

    def pause(self, message="Press Enter to continue..."):
        input(Fore.WHITE + "\n❯ " + message + Style.RESET_ALL)
    def __init__(self):

        self.player = None

        self.locations = {}

        self.current_location = None

        # Dark Cave starts hidden until the torch is lit.
        self.cave_lit = False

        self.game_running = True

        self.create_world()


    # =========================================
    # CREATE WORLD
    # =========================================

    def create_world(self):

        # -------------------------------------------------
        # ANCIENT FOREST — EXISTING PUZZLE, UPDATED ONLY
        # AS REQUESTED: moderate 30-second riddle, marked Hard.
        # -------------------------------------------------
        forest_puzzle = Puzzle(
            "Riddle",
            "I am a two-digit number.\n"
            "My digits add up to 9.\n"
            "My tens digit is twice my ones digit.\n"
            "What number am I?",
            "63",
            20,
            "Hard",
            30
        )

        # -------------------------------------------------
        # DARK CAVE — EXISTING LOGIC PUZZLE UNCHANGED.
        # -------------------------------------------------
        cave_puzzle = Puzzle(
            "Logic",
            "If 5 cats catch 5 mice in 5 minutes, how long for 1 cat to catch 1 mouse?",
            "5",
            30,
            "Medium",
            45
        )

        # -------------------------------------------------
        # ANCIENT LIBRARY — EXISTING CIPHER UNCHANGED.
        # Two additional Library stages are added after it.
        # -------------------------------------------------
        library_cipher = Puzzle(
            "Cipher",
            "Decode this message: UFTU",
            "test",
            40,
            "Hard",
            60
        )

        library_riddle = Puzzle(
            "Riddle",
            "I am always in front of you but can never be seen. What am I?",
            "future",
            30,
            "Medium",
            45
        )

        library_pattern = Puzzle(
            "Pattern",
            "Find the next number: 2, 6, 12, 20, 30, ?",
            "42",
            40,
            "Hard",
            60
        )

        # All three Library stages happen in the same location.
        self.library_puzzles = [
            library_cipher,
            library_riddle,
            library_pattern
        ]

        forest = Location(
            "Ancient Forest",
            """
A dark forest covered with fog.

An old path leads deeper into the unknown.
""",
            forest_puzzle
        )

        cabin = Location(
            "Abandoned Cabin",
            """
An old wooden cabin.

Something useful may be hidden here.
"""
        )

        cave = Location(
            "Dark Cave",
            """
A dangerous cave.

Strange sounds echo from the darkness.
""",
            cave_puzzle,
            "Ancient Key"
        )

        library = Location(
            "Ancient Library",
            """
A room filled with ancient books.

A secret message is hidden here.

Three hidden fragments of the Treasure Map are said to be
scattered among the library's challenges.
""",
            library_cipher
        )

        treasure = Location(
            "Treasure Room",
            """
A golden chamber.

The legendary treasure is here.
""",
            None,
            "Complete Treasure Map"
        )

        forest.add_connection(cabin)

        cabin.add_connection(forest)
        cabin.add_connection(cave)

        cave.add_connection(cabin)
        cave.add_connection(library)

        library.add_connection(cave)
        library.add_connection(treasure)

        self.locations = {
            "forest": forest,
            "cabin": cabin,
            "cave": cave,
            "library": library,
            "treasure": treasure
        }


    # =========================================
    # HUD DISPLAY
    # =========================================

    def display_hud(self):

        self.box(
            "PLAYER",
            [
                f"Explorer : {self.player.name}",
                f"Location : {self.current_location.name}",
                f"Health   : {self.player.health}/{self.player.max_health}",
                f"Score    : {self.player.score}",
                f"Items    : {len(self.player.inventory)}"
            ],
            Fore.CYAN
        )

    def show_map(self):

        self.clear_screen()
        current = self.current_location.name

        def marker(name, locked=False, unlocked=False):
            if current == name:
                return f"[CURRENT] {name}"
            if locked:
                return f"[LOCKED]  {name}"
            if unlocked:
                return f"[OPEN]    {name}"
            return f"          {name}"

        treasure = marker(
            "Treasure Room",
            locked="Treasure Map" not in self.player.inventory,
            unlocked="Treasure Map" in self.player.inventory
        )
        library = marker("Ancient Library")
        cave = marker(
            "Dark Cave",
            locked="Ancient Key" not in self.player.inventory,
            unlocked="Ancient Key" in self.player.inventory
        )
        cabin = marker("Abandoned Cabin")
        forest = marker("Ancient Forest")

        self.box(
            "TREASURE MAP",
            [
                treasure.center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                library.center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                cave.center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                cabin.center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                "|".center(self.get_ui_width() - 4),
                forest.center(self.get_ui_width() - 4)
            ],
            Fore.CYAN
        )

        self.box(
            "LEGEND",
            [
                "[CURRENT]  Current Location",
                "[OPEN]     Unlocked Location",
                "[LOCKED]   Locked Location",
                "[TREASURE] Treasure Room"
            ]
        )

        self.info(f" Current Location: {current}")
        self.pause()
    def start(self):

        self.clear_screen()

        self.box(
            "THE LOST TREASURE HUNT",
            [
                "A riddle-based scavenger hunt",
                "Solve puzzles. Collect clues. Find the treasure."
            ],
            Fore.MAGENTA
        )

        name = input(
            Fore.WHITE + "\n❯ Enter explorer name: " + Style.RESET_ALL
        ).strip()

        if not name:
            name = "Explorer"

        self.player = Player(name)
        self.current_location = self.locations["forest"]
        self.player.move_to(self.current_location)

        self.pause("Press Enter to begin the hunt...")
        self.game_loop()
    def game_loop(self):

        while self.game_running:

            self.dashboard()

            if not self.player.is_alive():
                break

            choice = input(
                Fore.WHITE + "❯ Choose option: " + Style.RESET_ALL
            ).strip()

            if choice == "1":
                self.explore()

            elif choice == "2":
                self.travel()

            elif choice == "3":
                self.clear_screen()
                inventory_lines = (
                    [f"• {item}" for item in self.player.inventory]
                    if self.player.inventory
                    else ["Inventory is empty."]
                )
                self.box("INVENTORY", inventory_lines, Fore.CYAN)
                self.pause()

            elif choice == "4":
                self.clear_screen()
                self.box(
                    "HUNT ENDED",
                    [
                        "Thank you for playing The Lost Treasure Hunt.",
                        "Your treasure hunt has ended."
                    ],
                    Fore.MAGENTA
                )
                self.game_running = False

            else:
                self.clear_screen()
                self.box(
                    "INVALID OPTION",
                    ["Please choose an option from 1 to 4."],
                    Fore.RED
                )
                self.pause()
    def explore(self):

        self.clear_screen()
        location = self.current_location

        # The Dark Cave remains unusable until the torch is lit.
        if location.name == "Dark Cave" and not self.cave_lit:
            self.light_dark_cave()
            return

        self.box(
            "EXPLORATION",
            [
                f" {location.name}",
                "You carefully examine the area."
            ],
            Fore.CYAN
        )

        time.sleep(0.7)

        description = [
            line.strip()
            for line in location.description.strip().splitlines()
            if line.strip()
        ]

        self.box("LOCATION", description)

        # The Ancient Library contains three sequential challenges.
        if location.name == "Ancient Library":
            for library_puzzle in self.library_puzzles:
                if not library_puzzle.is_completed():
                    self.solve_puzzle(library_puzzle)
                    self.find_items()
                    self.trigger_threat()
                    return

            self.box(
                "ANCIENT LIBRARY",
                [
                    "All three challenges are complete.",
                    "The three Treasure Map pieces are assembled.",
                    "The complete map is ready."
                ],
                Fore.GREEN
            )
            self.find_items()
            self.trigger_threat()
            return

        if location.has_puzzle():
            puzzle = location.puzzle
            if not puzzle.is_completed():
                self.solve_puzzle(puzzle)

        self.find_items()
        self.trigger_threat()

    def solve_puzzle(self, puzzle):

        self.clear_screen()

        puzzle_type = getattr(puzzle, "puzzle_type", "Puzzle")
        difficulty = getattr(puzzle, "difficulty", "Unknown")
        reward = getattr(puzzle, "reward", 0)
        time_limit = puzzle.get_time_limit()

        self.box(
            f"{puzzle_type.upper()} CHALLENGE",
            [
                f" Location   : {self.current_location.name}",
                f" Difficulty : {difficulty}",
                f" Reward     : +{reward} Score",
                f" Time Limit : {time_limit} seconds"
            ],
            Fore.MAGENTA
        )

        self.box("PUZZLE", [puzzle.question])

        self.warning(f" You have {time_limit} seconds to answer.")

        timer = GameTimer(time_limit)
        timer.start()

        answer = input(
            Fore.WHITE + "\n❯ Your Answer: " + Style.RESET_ALL
        )

        timer.stop()

        if timer.is_expired():

            self.clear_screen()
            self.box(
                "TIME'S UP",
                [
                    "You failed the challenge.",
                    " -10 Score"
                ],
                Fore.YELLOW
            )

            self.player.remove_score(10)
            self.pause()
            return

        if puzzle.check_answer(answer):

            self.clear_screen()
            self.box(
                "PUZZLE SOLVED",
                [
                    "✓ Correct Answer!",
                    f" +{reward} Score",
                    "The mechanism unlocks."
                ],
                Fore.GREEN
            )

            puzzle.solve()
            self.player.add_score(reward)

            # Ancient Forest Hard Riddle:
            # existing progression item + the new Torch Batteries.
            if (
                self.current_location.name == "Ancient Forest"
                and puzzle_type.lower() == "riddle"
            ):
                self.success("🗝 Ancient Key acquired!")
                self.player.add_item("Ancient Key")

                self.success("🔋 Torch Batteries acquired!")
                self.player.add_item("Torch Batteries")

            # Ancient Library stage 1: Cipher -> Map Piece 1.
            elif (
                self.current_location.name == "Ancient Library"
                and puzzle is self.library_puzzles[0]
            ):
                self.success("🗺 Treasure Map Piece 1 acquired!")
                self.player.add_item("Treasure Map Piece 1")

            # Ancient Library stage 2: Medium Riddle -> Map Piece 2.
            elif (
                self.current_location.name == "Ancient Library"
                and puzzle is self.library_puzzles[1]
            ):
                self.success("🗺 Treasure Map Piece 2 acquired!")
                self.player.add_item("Treasure Map Piece 2")

            # Ancient Library stage 3: Hard Pattern -> Map Piece 3
            # and assemble the complete Treasure Map.
            elif (
                self.current_location.name == "Ancient Library"
                and puzzle is self.library_puzzles[2]
            ):
                self.success("🗺 Treasure Map Piece 3 acquired!")
                self.player.add_item("Treasure Map Piece 3")

                self.success("🗺 The three map pieces fit together!")
                self.player.add_item("Complete Treasure Map")

            # The existing Dark Cave Logic puzzle stays exactly as it is.
            # After it is solved, reveal the class-purpose clue.
            if (
                self.current_location.name == "Dark Cave"
                and puzzle is self.locations["cave"].puzzle
            ):
                self.clear_screen()
                self.box(
                    "A CLUE IN THE DARK",
                    [
                        "A faded message appears on the cave wall:",
                        "",
                        '"What did we had on 22nd July"'
                    ],
                    Fore.CYAN
                )

            self.pause()

        else:

            self.clear_screen()
            self.box(
                "WRONG ANSWER",
                [
                    "✗ That answer is incorrect.",
                    "⚠ A trap has been activated.",
                    " -10 Health"
                ],
                Fore.RED
            )

            self.player.take_damage(10)
            self.pause()

    def light_dark_cave(self):
        """Mandatory torch-lighting sequence for the Dark Cave."""

        self.clear_screen()

        self.box(
            "DARK CAVE",
            [
                "????????????????????",
                "",
                "You step into the cave.",
                "It is completely dark.",
                "",
                "You cannot see the path ahead."
            ],
            Fore.WHITE
        )

        input(
            Fore.WHITE + "\n❯ Press Enter to light the torch..." + Style.RESET_ALL
        )

        if "Torch" not in self.player.inventory:
            self.box(
                "NO TORCH",
                [
                    "You cannot see anything.",
                    "You need a Torch to continue."
                ],
                Fore.RED
            )
            self.pause()
            return

        if "Torch Batteries" not in self.player.inventory:
            self.box(
                "TORCH HAS NO POWER",
                [
                    "You have a Torch, but no Torch Batteries.",
                    "Find the batteries before continuing."
                ],
                Fore.RED
            )
            self.pause()
            return

        # Lightweight terminal reveal. No extra library required.
        frames = [
            ("░" * 20, "The darkness begins to fade..."),
            ("▒" * 20, "The torch is getting brighter..."),
            ("▓" * 20, "The cave is becoming visible...")
        ]

        for frame, message in frames:
            self.clear_screen()
            self.box(
                "LIGHTING TORCH",
                [
                    frame,
                    "",
                    message
                ],
                Fore.YELLOW
            )
            time.sleep(0.25)

        self.cave_lit = True

        self.clear_screen()
        self.box(
            "DARK CAVE — ILLUMINATED",
            [
                "🔦 The torch lights up the cave.",
                "",
                "The path ahead is now visible.",
                "The darkness has been revealed."
            ],
            Fore.YELLOW
        )
        self.pause()

    def find_items(self):

        location = self.current_location

        if location.name == "Abandoned Cabin":
            if "Torch" not in self.player.inventory:

                self.clear_screen()
                self.box(
                    "HIDDEN ITEM",
                    [
                        "✨ You search the cabin carefully.",
                        "🔦 Torch found!"
                    ],
                    Fore.YELLOW
                )

                self.player.add_item("Torch")
                self.pause()

    def trigger_threat(self):

        chance = random.randint(1, 5)

        if chance == 3:

            trap = Threat(
                "Hidden Spike Trap",
                15,
                """
The floor collapses suddenly.

Sharp spikes appear.
"""
            )

            self.clear_screen()
            self.box(
                "THREAT DETECTED",
                [
                    "⚠ A hidden trap has been triggered.",
                    "Prepare yourself."
                ],
                Fore.RED
            )

            trap.activate(self.player)
            self.pause()
    def travel(self):

        self.clear_screen()
        location = self.current_location
        connections = location.connections

        lines = []

        for index, destination in enumerate(connections, start=1):

            if destination.requires_item():
                if destination.required_item in self.player.inventory:
                    status = "🔓 Unlocked"
                else:
                    status = f"🔒 Requires: {destination.required_item}"

                lines.append(
                    f"{index}  {destination.name}   {status}"
                )
            else:
                lines.append(
                    f"{index}  {destination.name}"
                )

        self.box("TRAVEL", lines, Fore.CYAN)

        choice = input(
            Fore.WHITE + "\n❯ Choose destination: " + Style.RESET_ALL
        ).strip()

        try:

            index = int(choice) - 1
            destination = connections[index]

            if destination.requires_item():
                if destination.required_item not in self.player.inventory:

                    self.box(
                        "LOCATION LOCKED",
                        [f"🔒 Required item: {destination.required_item}"],
                        Fore.RED
                    )
                    self.pause()
                    return

            self.clear_screen()
            self.box(
                "TRAVELLING",
                [f"🚶 Travelling to {destination.name}..."],
                Fore.CYAN
            )

            time.sleep(0.7)

            self.current_location = destination
            self.player.move_to(destination)

            if destination.name == "Treasure Room":
                self.win_game()
            else:
                self.pause()

        except (ValueError, IndexError):

            self.error("❌ Invalid destination!")
            self.pause()
    def win_game(self):

        self.clear_screen()

        self.box(
            " TREASURE ROOM",
            [
                "You have assembled the complete Treasure Map.",
                "",
                "A treasure chest stands before you.",
                "",
                "Press ENTER to open the treasure."
            ],
            Fore.YELLOW
        )

        input(
            Fore.WHITE
            + "❯ "
            + Style.RESET_ALL
        )

        self.clear_screen()

        self.box(
            " TREASURE OPENED",
            [
                " TREASURE ",
                "",
                "TREASURE AWARDED",
                "",
                "50 marks given by Dr. Farhana Ma'am",
                "",
                "Explorer        : " + self.player.name,
                "Final Score     : " + str(self.player.score),
                "Health          : " + f"{self.player.health}/{self.player.max_health}",
                "Items Collected : " + str(len(self.player.inventory)),
                "",
                "You completed The Lost Treasure Hunt."
            ],
            Fore.YELLOW
        )

        self.game_running = False

    def game_over(self):

        self.clear_screen()

        self.box(
            "💀 GAME OVER",
            [
                "Your health reached zero.",
                "The treasure remains undiscovered."
            ],
            Fore.RED
        )

        self.player.show_status()
        self.game_running = False