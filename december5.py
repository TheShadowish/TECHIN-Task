# Santa's Magical ASCII Countdown
"""
Santa Claus is preparing for Christmas Eve flight.
A magical countdown from 10 to 0 in ASCII art!
"""

import time
import os

# ASCII DIGITS ARRAY (0–9)
DIGITS = [
    [
        "                     ",
        "      000000000      ",
        "    00:::::::::00    ",
        "  00:::::::::::::00  ",
        " 0:::::::000:::::::0 ",
        " 0::::::0   0::::::0 ",
        " 0:::::0     0:::::0 ",
        " 0:::::0     0:::::0 ",
        " 0:::::0 000 0:::::0 ",
        " 0:::::0     0:::::0 ",
        " 0:::::0     0:::::0 ",
        " 0::::::0   0::::::0 ",
        " 0:::::::000:::::::0 ",
        "  00:::::::::::::00  ",
        "    00:::::::::00    ",
        "      000000000      "
    ],
    [
        "                     ",
        "       1111111       ",
        "      1::::::1       ",
        "     1:::::::1       ",
        "     1::::::1        ",
        "     1::::1          ",
        "     1::::1          ",
        "     1::::1          ",
        "     1::::l          ",
        "     1::::l          ",
        "     1::::l          ",
        "     1::::l          ",
        "  111::::::111       ",
        "  1::::::::::1       ",
        "  1::::::::::1       ",
        "  111111111111       "
    ],
    [
        "                     ",
        " 222222222222222     ",
        " 2:::::::::::::::22  ",
        " 2::::::222222:::::2 ",
        " 2222222     2:::::2 ",
        "             2:::::2 ",
        "             2:::::2 ",
        "          2222::::2  ",
        "     22222::::::22   ",
        "   22::::::::222     ",
        "  2:::::22222        ",
        " 2:::::2             ",
        " 2:::::2       222222",
        " 2::::::2222222:::::2",
        " 2::::::::::::::::::2",
        " 22222222222222222222"
    ],
    [
        "                     ",
        " 3333333333333333    ",
        " 3:::::::::::::::33  ",
        " 3::::::33333::::::3 ",
        " 3333333     3:::::3 ",
        "             3:::::3 ",
        "             3:::::3 ",
        "     33333333:::::3  ",
        "     3:::::::::::3   ",
        "     33333333:::::3  ",
        "             3:::::3 ",
        "             3:::::3 ",
        " 3333333     3:::::3 ",
        " 3::::::33333::::::3 ",
        " 3:::::::::::::::33  ",
        "  333333333333333    "
    ],
    [
        "                     ",
        "        444444444    ",
        "       4::::::::4    ",
        "      4::::::4       ",
        "      4:::::4        ",
        "     4:::::4         ",
        "    4::::4           ",
        "    4::::44::::4     ",
        "   4::::4 4::::4     ",
        "  4::::4  4::::4     ",
        " 4::::4   4::::4     ",
        " 4::::444444::::444  ",
        " 4::::::::::::::::4  ",
        " 4444444444:::::444  ",
        "           4::::4    ",
        "           4::::4    ",
        "         44::::::44  ",
        "         4::::::::4  ",
        "         4444444444  "
    ],
    [
        "                     ",
        " 555555555555555555  ",
        " 5::::::::::::::::5  ",
        " 5:::::555555555555  ",
        " 5:::::5             ",
        " 5:::::5             ",
        " 5:::::5555555555    ",
        " 5:::::::::::::::5   ",
        " 555555555555:::::5  ",
        "             5:::::5 ",
        "             5:::::5 ",
        " 5555555     5:::::5 ",
        " 5::::::55555::::::5 ",
        "  55:::::::::::::55  ",
        "    55:::::::::55    ",
        "      555555555      "
    ],
    [
        "                     ",
        "         66666666    ",
        "        6::::::6     ",
        "       6::::::6      ",
        "      6::::::6       ",
        "     6::::::6        ",
        "    6::::::6         ",
        "   6::::::::66666    ",
        "  6::::::::::::::6   ",
        " 6::::::66666:::::6  ",
        " 6:::::6     6:::::6 ",
        " 6:::::6     6:::::6 ",
        " 6::::::66666::::::6 ",
        "  66:::::::::::::66  ",
        "    66:::::::::66    ",
        "      666666666      "
    ],
    [
        "                     ",
        " 77777777777777777777",
        " 7::::::::::::::::::7",
        " 7::::::::::::::::::7",
        " 777777777777:::::::7",
        "            7::::::7 ",
        "           7::::::7  ",
        "          7::::::7   ",
        "         7::::::7    ",
        "        7::::::7     ",
        "       7::::::7      ",
        "      7::::::7       ",
        "     7::::::7        ",
        "    7::::::7         ",
        "   7::::::7          ",
        "  77777777           "
    ],
    [
        "                     ",
        "      888888888      ",
        "    88:::::::::88    ",
        "  88:::::::::::::88  ",
        " 8::::::88888::::::8 ",
        " 8:::::8     8:::::8 ",
        " 8:::::8     8:::::8 ",
        "  8:::::88888:::::8  ",
        "   8:::::::::::::8   ",
        "  8:::::88888:::::8  ",
        " 8:::::8     8:::::8 ",
        " 8:::::8     8:::::8 ",
        " 8::::::88888::::::8 ",
        "  88:::::::::::::88  ",
        "    88:::::::::88    ",
        "      888888888      "
    ],
    [
        "                     ",
        "      999999999      ",
        "    99:::::::::99    ",
        "  99:::::::::::::99  ",
        " 9::::::99999::::::9 ",
        " 9:::::9     9:::::9 ",
        " 9:::::9     9:::::9 ",
        "  9:::::99999::::::9 ",
        "   99::::::::::::::9 ",
        "     99999::::::::9  ",
        "          9::::::9   ",
        "         9::::::9    ",
        "        9::::::9     ",
        "       9:::::9       ",
        "      9:::::9        ",
        "     9999999         "
    ]
]

# Festive messages for each countdown phase
MESSAGES = [
    "Santa is preparing…",
    "Reindeer are buckling up…",
    "Sleigh warming up…",
    "Checking the naughty-nice list…",
    "Gifts are secure…",
    "Rudolph's nose is glowing…",
    "Elves are waving goodbye…",
    "Final countdown…",
    "Almost there…",
    "3… 2… 1…",
    "Hold on tight!"
]


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_number(number):
    """
    Display ASCII art for a given number.
    
    Args:
        number: Integer from 0 to 9
    """
    if number < 0 or number > 9:
        return
    
    digit_art = DIGITS[number]
    for line in digit_art:
        print(line)


def countdown():
    """
    Perform the magical countdown from 10 to 0.
    """
    messages = MESSAGES.copy()
    
    for count in range(10, -1, -1):
        clear_screen()
        
        print(f"\n{'='*50}")
        print(f"Timer: {count}")
        print(f"{'='*50}\n")
        
        # Display the ASCII art number
        if count == 10:
            # For 10, display both digits
            print("   ", end="")
            display_number(1)
        else:
            display_number(count)
        
        # Display a festive message
        if messages:
            message = messages.pop(0)
            print(f"\n{message}")
        
        # Wait 1 second before next countdown
        time.sleep(1)
    
    # Final launch message
    clear_screen()
    print("\n" * 5)
    print("🎅" * 20)
    print("\n" * 2)
    print("✨" * 15)
    print(" SANTA'S SLEIGH IS LAUNCHING! ".center(60))
    print("✨" * 15)
    print("\n" * 2)
    print("🎅" * 20)
    print("\n" * 5)
    print("Merry Christmas! 🎄")
    print("\n")


def main():
    """Main function to start the countdown."""
    try:
        input("Press ENTER to start Santa's magical countdown... 🎅\n")
        countdown()
    except KeyboardInterrupt:
        print("\n\nCountdown interrupted! Santa will try again tomorrow.")
    except Exception as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
