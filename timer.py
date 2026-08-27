"""
timer.py

Handles live countdown timer
for timed puzzles.
"""

import time
import threading


class GameTimer:

    def __init__(self, time_limit):

        self.time_limit = time_limit
        self.remaining = time_limit

        self.running = False

        self.thread = None



    def start(self):

        self.remaining = self.time_limit

        self.running = True

        self.thread = threading.Thread(
            target=self.countdown
        )

        self.thread.daemon = True

        self.thread.start()



    def countdown(self):

        while self.running and self.remaining > 0:

            time.sleep(1)

            self.remaining -= 1



    def display(self):

        minutes = self.remaining // 60

        seconds = self.remaining % 60


        if self.remaining <= 5:

            print(
                f"\n⚠️ Hurry! {seconds} seconds remaining!"
            )


        else:

            print(
                f"\n⏳ Time Remaining: {minutes:02}:{seconds:02}"
            )



    def is_expired(self):

        return self.remaining <= 0



    def stop(self):

        self.running = False



    def reset(self):

        self.stop()

        self.remaining = self.time_limit



    def get_remaining(self):

        return self.remaining