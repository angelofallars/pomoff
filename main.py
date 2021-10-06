#!/bin/python3

import time
import os
import math as m
from getch import getch
import config as cf


def clear():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


class Interval:
    def __init__(self, duration, session_type, end_icon="emblem_information"):
        # length of the interval in minutes
        self.duration = duration

        # the type of session, work, short/long break
        self.session_type = session_type

        # name of the icon used for the zenity end message
        self.end_icon = end_icon


def start_interval(interval):
    """Start an interval (Pomodoro, short break or long break)"""
    clock_hands = ("|", "/", "-", "\\", "|", "/", "-", "\\")

    # Counter is for changing the clock hands
    counter = 0

    start_time = time.perf_counter()
    elapsed_time = 0

    # Last time is for the clock hands to keep it turning at a steady rate
    last_time = 0

    duration_seconds = interval.duration * 60

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

        clear()
        print(f"🍅 - {interval.session_type}")
        print(f"[{clock_hands[counter]}] ", end="")
        print(f"{minutes}m {seconds}s")

        time.sleep(0.25)

    return True


def broadcast(text, icon="emblem_information"):
    """Broadcast a message warning to the user with Zenity.

    args
      text - The text that will be displayed on the message window
      icon - The icon beside the text"""

    os.system(f"zenity --icon-name={icon} --warning \
               --width=200 --text '{text}'")


def broadcast_ending(interval: Interval):
    """Broadcast the ending of an interval with Zenity.

    args
      interval - The interval, can be work, short break or long break"""

    broadcast(text=f"{interval.session_type.upper()} OVER\n\
{interval.duration} minutes have passed.",
              icon=interval.end_icon)


def main():
    work_time = Interval(cf.work_time, "work", end_icon="emblem-success")
    short_break = Interval(cf.short_break_time, "short break")
    long_break = Interval(cf.long_break_time, "long break")

    while True:
        clear()

        print("POMOFF")
        print(f"[s] {cf.session_intervals}-Pom Session \
({cf.work_time * cf.session_intervals}m + \
{cf.short_break_time * (cf.session_intervals - 1)}m)")
        print(f"[j] Work ({cf.work_time}m)")
        print(f"[k] Short break ({cf.short_break_time}m)")
        print(f"[l] Long break ({cf.long_break_time}m)")
        print("[q] Quit")

        char = getch().lower()

        # ===============
        # = SESSION     =
        # ===============
        if char == "s":
            for i in range(cf.session_intervals):
                start_interval(work_time)
                broadcast_ending(work_time)

                if i < cf.session_intervals - 1:
                    start_interval(short_break)
                    broadcast_ending(short_break)
                # The last break should be a long break
                else:
                    start_interval(long_break)
                    broadcast_ending(long_break)

        # ===============
        # = WORK TIME   =
        # ===============
        if char == "j":
            start_interval(work_time)
            broadcast_ending(work_time)

        # ===============
        # = SHORT BREAK =
        # ===============
        if char == "k":
            start_interval(short_break)
            broadcast_ending(short_break)

        # ===============
        # = LONG BREAK  =
        # ===============
        if char == "l":
            start_interval(long_break)
            broadcast_ending(long_break)

        # ===============
        # = QUIT        =
        # ===============
        if char == "q":
            break

    return 0


if __name__ == "__main__":
    main()
