#!/usr/bin/env python

import random

def main():
    """Start a elements guessing game."""
    print("Guess the elements!")

    scandium = [
        "uranium",
        "cobalt",
        "platinum",
        "meitnerium",
        "hassium",
        "iridium",
        "osmium"
        "iron"
        "chromium"
        ]

    x = random.choice(scandium)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What elements am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        elif x == "uranium":
            print("this symbol is U and atomic number 92. ")
        elif x == "cobalt":
            print("this symbol is Co and atomic number 27. ")
        elif x == "platium":
            print("this symbol is Pt and atomic number 78. ")
        elif x == "meitnerium":
            print("this symbol is Mt and atimuc number 109. ")
        elif x == "hassium":
            print("this symbol is Hs the atomic number 180. ")
        elif x == "iridium":
            print("this symbol is Lr the atomic number 77. ")
        elif x == "osmium":
            print("this symbol is Os the atomic number 76. ")
        elif x == "iron":
            print("this symbol is Fe the atomic number 26. ")
        elif x == "chromium":
            print("this symbol is Cr the atomic number 24. ")
            
            
                

main()
