#!/usr/bin/env python3
from time import sleep


def input_answer(prompt, answer):
    user_input = input(prompt)
    if user_input == answer:
        return 1
    else:
        return 0


def main():
    # Question 1
    if not input_answer("What is the value of dh after line 129 executes? (Answer with a one-byte hex value, prefixed with '0x')\n", "0x00"):
        return 0

    # Question 2
    if not input_answer("\nWhat is the value of gs after line 145 executes? (Answer with a one-byte hex value, prefixed with '0x')\n", "0x00"):
        return 0

    # Question 3
    if not input_answer("\nWhat is the value of si after line 151 executes? (Answer with a two-byte hex value, prefixed with '0x')\n", "0x0000"):
        return 0

    # Question 4
    if not input_answer("\nWhat is the value of ax after line 169 executes? (Answer with a two-byte hex value, prefixed with '0x')\n", "0x0e74"):
        return 0

    # Question 5
    if not input_answer("\nWhat is the value of ax after line 199 executes for the first time? (Answer with a two-byte hex value, prefixed with '0x')\n", "0x0e61"):
        return 0

    # Question 6
    if not input_answer("\If the value of bp at line 313 is 0x9000 what is the value of bp after line 335 executes? (Answer with a two-byte hex value, prefixed with '0x')\n", "0x9000"):
        return 0

    # Question 7
    if not input_answer("\If the value of sp at line 313 is 0xaaaa what is the value of sp after line 335 executes? (Answer with a two-byte hex value, prefixed with '0x')\n", "0xaaa0"):
        return 0

    # Question 8
    if not input_answer("\If the value of sp at line 313 is 0xaaaa what is the value of sp after line 335 executes? (Answer with a two-byte hex value, prefixed with '0x')\n", "0xaaaa"):
        return 0

    return 1


if __name__ == "__main__":
    print("\nWelcome!\n")

    if(main()):
        print("flag{reeeeeee3333eeally_go0d_job_solv1ng_your_fir5t_rev_reee33334eeeeeecrui7!}")
    else:
        print("Sorry, try again!")
