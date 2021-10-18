#!/bin/python3

import time
import os
import math as m
from helpers.getch import getch
import config.config as cf
import colorama

# Colors for the terminal
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
BOLD = "\033[1m"
DIM = colorama.Style.DIM
RESET = colorama.Style.RESET_ALL


def clear():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


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
        print(f"{RED}🍅{RESET} {BOLD}{self.session_type.upper()}{RESET}")

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
            print(f"   [{RED}{clock_hands[counter]}{RESET}] {DIM}{minutes}m {seconds}s{RESET}     ",
            end="\r")

            time.sleep(0.25)

        return 0


def play_sound(sound_file):
    """Play a sound from the program's /sound directory

    parameters
        sound_file - name of the sound file to play in /sound"""

    program_directory = os.path.dirname(__file__)
    sound_file = os.path.join(program_directory, "sound/", sound_file)

    # Use sox to play sound
    os.system(f"play -v 1.2 {sound_file} > /dev/null 2>&1 &")


def broadcast(text_head, text_body):
    """Broadcast a message warning to the user with notify-send.

    parameters
      text_head - The title of the notification
      text-body - The body of the notification"""

    os.system(f'notify-send "{text_head}" "{text_body}"')


def broadcast_ending(interval: Interval):
    """Broadcast the ending of an interval with notify-send.

    parameters
      interval - The interval, can be work, short break or long break"""

    play_sound(cf.end_sound)
    broadcast(text_head=f"{interval.session_type.upper()} OVER",
              text_body=f"{interval.duration} minutes have passed.")


def main():
    work_time = Interval(cf.work_time, "work")
    short_break = Interval(cf.short_break_time, "short break")
    long_break = Interval(cf.long_break_time, "long break")

    while True:
        clear()

        # Menu
        print(f"{RED}{BOLD}POMOFF{RESET}")
        print(f"[{RED}s{RESET}] {cf.session_intervals}-Pom Session \
{DIM}({cf.work_time * cf.session_intervals}m + \
{cf.short_break_time * (cf.session_intervals - 1)}m){RESET}")
        print(f"[{RED}j{RESET}] Work {DIM}({cf.work_time}m){RESET}")
        print(f"[{RED}k{RESET}] Short break {DIM}({cf.short_break_time}m){RESET}")
        print(f"[{RED}l{RESET}] Long break {DIM}({cf.long_break_time}m){RESET}")
        print(f"[{RED}q{RESET}] Quit")

        char = getch().lower()

        # ===============
        # = SESSION     =
        # ===============
        if char == "s":
            for i in range(cf.session_intervals):
                work_time.start()
                broadcast_ending(work_time)

                if i < cf.session_intervals - 1:
                    short_break.start()
                    broadcast_ending(short_break)
                # The last break should be a long break
                else:
                    long_break.start()
                    broadcast_ending(long_break)

        # ===============
        # = WORK TIME   =
        # ===============
        if char == "j":
            work_time.start()
            broadcast_ending(work_time)

        # ===============
        # = SHORT BREAK =
        # ===============
        if char == "k":
            short_break.start()
            broadcast_ending(short_break)

        # ===============
        # = LONG BREAK  =
        # ===============
        if char == "l":
            long_break.start()
            broadcast_ending(long_break)

        # ===============
        # = QUIT        =
        # ===============
        if char == "q":
            break

    return 0


if __name__ == "__main__":
    main()
