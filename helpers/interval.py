import time
import math as m

# Necessary to get config from another directory
import sys
sys.path.append("..")

import helpers.colors as c
from config.config import end_sound
from config.config import notify_icon
from helpers.notify import broadcast
from helpers.clear import clear
from helpers.sound import play_sound


class Interval:
    def __init__(self, duration, session_type):
        # length of the interval in minutes
        self.duration = duration

        # the type of session, work, short/long break
        self.session_type = session_type


    def start(self):
        """Start this Pomodoro interval."""
        clock_hands = ("|", "/", "-", "\\", "|", "/", "-", "\\")

        # Counter is for changing the clock hands
        counter = 0

        start_time = time.perf_counter()
        elapsed_time = 0

        # Last time is for the clock hands to keep it turning at a steady rate
        last_time = 0
        duration_seconds = self.duration * 60

        # Print the session type
        clear()
        print(f"{c.RED}🍅{c.RESET} {c.BOLD}{self.session_type.upper()}{c.RESET}")

        while elapsed_time < duration_seconds:

            current_time = time.perf_counter()
            elapsed_time = current_time - start_time
            remaining_time = duration_seconds - elapsed_time

            # Iterate through the clock hands animation
            if elapsed_time >= last_time + 0.5:
                counter += 1
                last_time = elapsed_time

                if counter >= len(clock_hands):
                    counter = 0

            # Ceiling instead of round so that the starting time is "25m 0s"
            # instead of "24m 60s"
            seconds = m.ceil(remaining_time) % 60
            minutes = m.ceil(remaining_time) // 60

            # Print the fancy animation and time left, updated
            print(f"   [{c.RED}{clock_hands[counter]}{c.RESET}] {c.DIM}{minutes}m \
{seconds}s{c.RESET}     ",
            end="\r")

            time.sleep(0.25)

        play_sound(end_sound)
        broadcast(text_head=f"{self.session_type.upper()} OVER",
                  text_body=f"{self.duration} minutes have passed.",
                  icon=notify_icon)
        return 0
