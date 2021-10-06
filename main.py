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
        # self.duration is the length of the interval in minutes
        self.duration = duration
        self.session_type = session_type

        # end_icon is the name of the icon used for the zenity end message
        self.end_icon = end_icon


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
        print("POMODORO TIMER")
        print(f"[s] 4-Pom Session ({cf.work_time * 4} minutes + \
{cf.short_break_time * 3} minutes)")
        print(f"[j] Work time ({cf.work_time} minutes)")
        print(f"[k] Short break ({cf.short_break_time} minutes)")
        print(f"[l] Long break ({cf.long_break_time} minutes)")
        print("[q] Quit")
        char = getch().lower()

        # ===============
        # = SESSION     =
        # ===============
        if char == "s":
            for i in range(4):
                start_interval(work_time)
                broadcast_ending(work_time)

                # The last break should be a long break
                if i < 3:
                    start_interval(short_break)
                    broadcast_ending(short_break)
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
