#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program changes the number of a month to its word counterpart


def main():
    # This function changes the number of a month to its word counterpart

    # Input
    month = int(input("Enter a month in the form of a number (1-12): "))
    print("")

    # Process & Output
    if month == 1:
        print("The 1st Month is January!")
    elif month == 2:
        print("The 2nd Month is February!")
    elif month == 3:
        print("The 3rd Month is March!")
    elif month == 4:
        print("The 4th Month is April!")
    elif month == 5:
        print("The 5th Month is May!")
    elif month == 6:
        print("The 6th Month is June!")
    elif month == 7:
        print("The 7th Month is July!")
    elif month == 8:
        print("The 8th Month is August!")
    elif month == 9:
        print("The 9th Month is September!")
    elif month == 10:
        print("The 10th Month is October!")
    elif month == 11:
        print("The 11th Month is November!")
    elif month == 12:
        print("The 12th and Last Month is December!")
    else:
        print("That is not a valid month!")


if __name__ == "__main__":
    main()
