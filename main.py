#!/usr/bin/python3
import config.config as cf
import modules.interval as interval
import modules.colors as c
from modules.clear import clear
from modules.getch import getch
import sys


def launch(time):
    """
    A function to launch the timer
    """
    chrono = interval.Interval(time, "work", cf)
    chrono.start()


def usage():
    """
    Print the usage text.
    """
    print(f"Usage: pomoff [option] ...")
    print( """  -h, help               see this help page
  -w, work               launch a work interval
  -b, break, shortbreak  launch a short break interval
 -lb, longbreak          launch a long break interval

The config file is located in the /config directory of the pomoff folder.""")


def main():

    while True:
        clear()
        # Menu
        print(f"{c.RED}{c.BOLD}POMOFF{c.RESET}")
        print(f"[{c.RED}s{c.RESET}] {cf.session_intervals}-Pom Session \
{c.DIM}({cf.work_time * cf.session_intervals}m + \
{cf.short_break_time * (cf.session_intervals - 1)}m){c.RESET}")
        print(f"[{c.RED}j{c.RESET}] Work {c.DIM}({cf.work_time}m){c.RESET}")
        print(f"[{c.RED}k{c.RESET}] Short break {c.DIM}({cf.short_break_time}m){c.RESET}")
        print(f"[{c.RED}l{c.RESET}] Long break {c.DIM}({cf.long_break_time}m){c.RESET}")
        print(f"[{c.RED}q{c.RESET}] Quit")

        char = getch().lower()

        # ===============
        # = SESSION     =
        # ===============
        if char == "s":
            for i in range(cf.session_intervals):
                work_time.start()

                if i < cf.session_intervals - 1:
                    short_break.start()
                # The last break should be a long break
                else:
                    long_break.start()

        # ===============
        # = WORK TIME   =
        # ===============
        if char == "j":
            work_time.start()

        # ===============
        # = SHORT BREAK =
        # ===============
        if char == "k":
            short_break.start()

        # ===============
        # = LONG BREAK  =
        # ===============
        if char == "l":
            long_break.start()

        # ===============
        # = QUIT        =
        # ===============
        if char == "q":
            break

    return 0


if __name__ == "__main__":
    work_time = interval.Interval(cf.work_time, "work", cf)
    short_break = interval.Interval(cf.short_break_time, "short break", cf)
    long_break = interval.Interval(cf.long_break_time, "long break", cf)

    # ===============
    # = MAIN MENU   =
    # ===============
    if len(sys.argv) == 1:
        main()

    # ===================
    # = CONFIGURE TIMER =
    # ===================
    elif '-w' in sys.argv or 'work' in sys.argv:
        work_time.start()

    elif '-b' in sys.argv or 'break' in sys.argv or 'shortbreak' in sys.argv:
        short_break.start()

    elif '-lb' in sys.argv or 'longbreak' in sys.argv:
        long_break.start()

    # ===================
    # = INVALID ARGUMENT=
    # ===================   
    else :
        usage()

"""CREDITS
"Bike, Bell Ding, Single, 01-01.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org
"Bell, Counter, A.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org
"""
