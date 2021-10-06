import time
import os
import math as m
from getch import getch


# Durations for each Pomodoro clock part
WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 15


def clear():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


class Interval:
    def __init__(self, duration, session_type):
        # self.duration is the length of the interval in minutes
        self.duration = duration
        self.session_type = session_type


def start_interval(interval):
    """Start an interval (Pomodoro, short break or long break)"""
    clock_hands = ("|", "/", "-", "\\", "|", "/", "-", "\\")

    start_time = time.perf_counter()
    elapsed_time = 0

    duration_seconds = interval.duration * 60

    while elapsed_time < duration_seconds:

        # For loop for the fancy "clock" animation
        for i in range(len(clock_hands)):
            current_time = time.perf_counter()
            elapsed_time = current_time - start_time
            remaining_time = duration_seconds - elapsed_time

            # Ceiling instead of round so that the starting time is "25m 0s"
            # instead of "24m 60s"
            seconds = m.ceil(remaining_time) % 60
            minutes = m.ceil(remaining_time) // 60

            clear()
            print(f"🍅 - {interval.session_type}")
            print(f"[{clock_hands[i]}] ", end="")
            print(f"{minutes}m {seconds}s")

            time.sleep(0.50)

    return True


def main():
    work_time = Interval(WORK_TIME, "work")
    short_break = Interval(SHORT_BREAK_TIME, "short break")
    long_break = Interval(LONG_BREAK_TIME, "long break")

    while True:
        clear()
        print("POMODORO TIMER")
        print(f"[s] 4-Pom Session ({WORK_TIME * 4} minutes + \
{SHORT_BREAK_TIME * 3} minutes)")
        print(f"[j] Work time ({WORK_TIME} minutes)")
        print(f"[k] Short break ({SHORT_BREAK_TIME} minutes)")
        print(f"[l] Long break ({LONG_BREAK_TIME} minutes)")
        print("[q] Quit")
        char = getch().lower()

        # ===============
        # = SESSION     =
        # ===============
        if char == "s":
            for i in range(4):
                start_interval(work_time)
                os.system(f"zenity --icon-name=emblem-success --warning \
                           --width=200 --text \
                           'WORK TIME OVER\n\
{WORK_TIME} minutes has passed'")

                # The last break should be a long break
                if i < 3:
                    start_interval(short_break)
                    os.system(f"zenity --icon-name=emblem-information --warning \
                               --width=200 --text \
                               'SHORT BREAK OVER\n\
{SHORT_BREAK_TIME} minutes has passed'")
                else:
                    start_interval(long_break)
                    os.system(f"zenity --icon-name=emblem-information --warning \
                               --width=200 --text \
                               'LONG BREAK OVER\n\
{LONG_BREAK_TIME} minutes has passed'")

        # ===============
        # = WORK TIME   =
        # ===============
        if char == "j":
            start_interval(work_time)
            os.system(f"zenity --icon-name=emblem-success --warning \
                       --width=200 --text \
                       'WORK TIME OVER\n\
{WORK_TIME} minutes has passed'")

        # ===============
        # = SHORT BREAK =
        # ===============
        if char == "k":
            start_interval(short_break)
            os.system(f"zenity --icon-name=emblem-information --warning \
                       --width=200 --text \
                       'SHORT BREAK OVER\n\
{SHORT_BREAK_TIME} minutes has passed'")

        # ===============
        # = LONG BREAK  =
        # ===============
        if char == "l":
            start_interval(long_break)
            os.system(f"zenity --icon-name=emblem-information --warning \
                       --width=200 --text \
                       'LONG BREAK OVER\n\
{LONG_BREAK_TIME} minutes has passed'")

        # ===============
        # = QUIT        =
        # ===============
        if char == "q":
            break

    return 0


if __name__ == "__main__":
    main()
