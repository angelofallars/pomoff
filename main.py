import time
import os

# Durations for each Pomodoro clock part
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 15


def clear():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clock_hands = ("-", "\\", "|", "/", "-", "\\", "|", "/")
    start_time = time.perf_counter()

    while True:
        for i in range(len(clock_hands)):
            current_time = time.perf_counter()
            elapsed_time = current_time - start_time

            clear()
            print(f"({clock_hands[i]}) {elapsed_time:0.0f}s")
            time.sleep(0.50)


if __name__ == "__main__":
    main()
