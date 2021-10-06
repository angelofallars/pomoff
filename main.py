import time
import os
import math as m
from getch import getch


# Durations for each Pomodoro clock part
WORK_TIME_DURATION = 25
SHORT_BREAK_DURATION = 5
LONG_BREAK_DURATION = 15


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

            seconds = m.ceil(remaining_time) % 60
            minutes = m.ceil(remaining_time) // 60

            clear()
            print(f"{interval.session_type}")
            print(f"[{clock_hands[i]}] ", end="")
            print(f"{minutes}m {seconds}s")

            time.sleep(0.50)

    return True


def main():
    work_time = Interval(WORK_TIME_DURATION, "work")
    short_break = Interval(SHORT_BREAK_DURATION, "short break")
    long_break = Interval(LONG_BREAK_DURATION, "long break")

    while True:
        clear()
        print("POMODORO TIMER")
        print(f"[j] Work time ({WORK_TIME_DURATION} minutes)")
        print(f"[k] Short break ({WORK_TIME_DURATION} minutes)")
        print(f"[l] Long break ({WORK_TIME_DURATION} minutes)")
        print("[q] Quit")
        char = getch().lower()

        if char == "j":
            start_interval(work_time)
        if char == "k":
            start_interval(short_break)
        if char == "l":
            start_interval(long_break)
        if char == "q":
            break

    return 0


if __name__ == "__main__":
    main()
