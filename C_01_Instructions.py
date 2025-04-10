# *************************************
# * Name: Roll It 13                  *
# * Author: Talon                     *
# * Purpose: Be able to play Roll It  *
# * 13 with user/computer             *
# *************************************

# functions go here


def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check if the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


# Main routine

# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Displays hte instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
