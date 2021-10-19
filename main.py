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
    chrono = interval.Interval(time, "work")
    chrono.start()

def main():
    work_time = interval.Interval(cf.work_time, "work")
    short_break = interval.Interval(cf.short_break_time, "short break")
    long_break = interval.Interval(cf.long_break_time, "long break")

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

    # ===============
    # = MAIN MENU   =
    # ===============
    if len(sys.argv) == 1:
        main()

    # ===============
    # = HELP PAGE   =
    # ===============
    elif '-h' in sys.argv or '--help' in  sys.argv: 
        print(f"\n{c.GREEN}{c.BOLD}Usage: POMOFF [option] ...{c.RESET}")
        print( """
            -h --help See the help page
            -w --work [integer] Launch the timer
        """)

    # ===================
    # = CONFIGURE TIMER =
    # ===================
    elif '-W' in sys.argv or '--work' in sys.argv:
        if len(sys.argv) > 2:
            if sys.argv[2].isnumeric() :
                launch(int(sys.argv[2]))
            else :
                print(f"{c.RED} {c.BOLD} -- Invalid argument {c.RESET}") 
                print("""Try: \n$  --help for more information \n """)
        else:
            print(f"{c.RED} {c.BOLD} -- Invalid argument {c.RESET}") 
            print("""Try: \n$  --help for more information \n """)

    # ===================
    # = INVALID ARGUMENT =
    # ===================   
    else :
        print(f"{c.RED} {c.BOLD} -- Invalid argument {c.RESET}") 
        print("""Try: \n$  --help for more information \n """)

"""CREDITS
"Bike, Bell Ding, Single, 01-01.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org
"Bell, Counter, A.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org
"""
