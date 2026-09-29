import random

def getvalidint(string: str) -> int:
    """Prompts the user repeatedly until a valid int is given.""" 
    validint = input("Enter a number: ")
    while validint.isdigit() == False:
        print("That is not a valid number. Try again.") 
        validint = input("Enter a number: ")
    validint = int(validint)

min = getvalidint("Enter the minimum num: ")
max = getvalidint("Enter the minimum num: ")
target = random.randint

def get_validint_within_range(min:int, max:int) -> int:
    """Repeatedly calls getvalidint until an int withing valid range is given."""
    if min < max and max > min:
        return input(f"Enter a guess of a number between {min} and {max}: ")
    else:
        print("Not a valid range.")
        getvalidint()

def playUserrounds(min:int, max:int, target:int) -> int:
    """Repeatedly calls get_valid_int_within_range and stores the guesses in a list, until the guess == the target.
    Then returns the list, Provides messaging after each guess (correct, too high, too low)"""
    get_validint_within_range()

def playCMProunds(min:int, max:int, target:int) -> int:
    """Repeatedly binary search logic to find the target number.
    Each Guess is stored in a list. Math used to generate guess is printed.
    List of guesses returned."""
    print()

def printoutcome(userrounds: list, cmprounds: list) -> str:
    """Print a report showing the guesses for each, determines the winner."""
    print()

def playagain() -> bool:
    """Repeatedly asks the user of they wish to play again until a valid response is given. Returns true if they want to play again, otherwise false."""
    print()

while True:
   userGuesses = playUserrounds(min, max, target)
   compGuesses = playCMProunds(min, max, target)
   printoutcome(userGuesses, compGuesses)
   if playagain():
       target = random.randint
   else:
        print("Have a good day!")
        break