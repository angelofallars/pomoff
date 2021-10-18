#!/bin/python3
import math as m
import config.config as cf
import helpers.interval as interval
import helpers.colors as c
from helpers.clear import clear
from helpers.getch import getch


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
    main()
