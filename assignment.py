import random

def getvalidint(string: str) -> int:
    """Prompts the user repeatedly until a valid int is given.""" 
    validint = input("Enter a number: ")
    while validint.isdigit() == False:
        print("That is not a valid number. Try again.") 
        validint = input("Enter a number: ")
    validint = int(validint)
    string = validint
    return string

def get_validint_within_range(min:int, max:int, target:int, userguess:str) -> int:
    """Repeatedly calls getvalidint until an int withing valid range is given."""
    while min == max:
        print("Not a valid min and max.")
        min = getvalidint(3)
        max = getvalidint(4)
    if min < target and target < max:
        userguess = input(f"Enter a guess of a number between {min} and {max}: ")
        if userguess.isdigit() != True or min < userguess and userguess < max:
            print("Not a valid guess.")
            getvalidint(7)
        else:
            return userguess
    else:
        min = getvalidint(5)
        max = getvalidint(6)

def playUserrounds(min:int, max:int, target:int, userguess:int) -> int:
    """Repeatedly calls get_valid_int_within_range and stores the guesses in a list, until the guess == the target.
    Then returns the list, Provides messaging after each guess (correct, too high, too low)"""
    get_validint_within_range(min, max, target, userguess)

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

min1 = getvalidint(1)
max1 = getvalidint(2)
target1 = random.randint(min1, max1)
user = []

while True:
   userGuesses = playUserrounds(min1, max1, target1, user)
   compGuesses = playCMProunds(min1, max1, target1)
   printoutcome(userGuesses, compGuesses)
   if playagain():
       target = random.randint
   else:
        print("Have a good day!")
        break