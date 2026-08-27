"""
puzzle.py

Handles different puzzle types:
- Riddle
- Logic
- Cipher
"""


class Puzzle:


    def __init__(
        self,
        puzzle_type,
        question,
        answer,
        reward,
        difficulty,
        time_limit=30
    ):

        self.puzzle_type = puzzle_type

        self.question = question

        self.answer = answer

        self.reward = reward

        self.difficulty = difficulty

        self.time_limit = time_limit

        self.completed = False



    # ==================================
    # DISPLAY PUZZLE
    # ==================================

    def display_puzzle(self):

        print("\n" + "=" * 40)


        if self.puzzle_type.lower() == "riddle":

            print("🧩 RIDDLE PUZZLE")


        elif self.puzzle_type.lower() == "logic":

            print("🧠 LOGIC PUZZLE")


        elif self.puzzle_type.lower() == "cipher":

            print("🔐 CIPHER PUZZLE")


        else:

            print("🧩 PUZZLE")



        print("=" * 40)


        print(
            f"Difficulty : {self.difficulty}"
        )


        print(
            f"Reward     : ⭐ {self.reward}"
        )


        print(
            f"Time Limit : ⏳ {self.time_limit} seconds"
        )


        print("\nQuestion:")

        print(self.question)


        print("=" * 40)



    # ==================================
    # CHECK ANSWER
    # ==================================

    def check_answer(self, player_answer):

        return (
            player_answer.lower().strip()
            ==
            self.answer.lower().strip()
        )



    # ==================================
    # COMPLETE PUZZLE
    # ==================================

    def solve(self):

        self.completed = True



    # ==================================
    # STATUS
    # ==================================

    def is_completed(self):

        return self.completed



    # ==================================
    # INFORMATION
    # ==================================

    def get_type(self):

        return self.puzzle_type



    def get_time_limit(self):

        return self.time_limit