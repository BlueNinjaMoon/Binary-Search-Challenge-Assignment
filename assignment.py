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
        if userguess.isdigit() != True:
            print("Not a valid guess.")
            userguess = getvalidint(7)
        else:
            userguess = int(userguess)
        if min > userguess and userguess > max:
            print("Not a valid guess.")
            userguess = getvalidint(8)
            userguess = int(userguess)
        else:
            return user.append(userguess)
    else:
        min = getvalidint(5)
        max = getvalidint(6)

def playUserrounds(min:int, max:int, target:int, userguess:int) -> int:
    """Repeatedly calls get_valid_int_within_range and stores the guesses in a list, until the guess == the target.
    Then returns the list, Provides messaging after each guess (correct, too high, too low)"""
    userindex = 0
    print(target1)
    while userguess.count(target) != True:
        get_validint_within_range(min, max, target, userguess)
        if userguess[userindex] < target:
            print("Too low of a guess.")
        else:
            if userguess[userindex > target]:
                print("Too high of a guess.")
            else:
                None
        userindex += 1
    print("You found the number!")
    userindex = userindex + 1
    return userindex

def playCMProunds(min:int, max:int, target:int, cmpguess) -> int:
    """Repeatedly binary search logic to find the target number.
    Each Guess is stored in a list. Math used to generate guess is printed.
    List of guesses returned."""
    cmpindex = 0
    while cmpguess.count(target) != True:
        middle = (min+max)//2
        print(f"Low {min} High {max} Middle Guess {middle}")
        if middle < target:
            print("Too low.")
            min = middle
        elif middle > target:
            print("Too high.")
            max = middle
        elif middle == target:
            print("Found target number.")
            break
        else:
            break
        cmp.append(cmpguess)
        cmpindex += 1
    cmpindex = cmpindex + 1
    return cmpindex

def printoutcome(userrounds: list, cmprounds: list) -> str:
    """Print a report showing the guesses for each, determines the winner."""
    print(f"You guessed {userrounds} time(s), and the computer took {cmprounds} guess(es).")

def playagain() -> bool:
    """Repeatedly asks the user of they wish to play again until a valid response is given. Returns true if they want to play again, otherwise false."""
    userinput = input("Do you wish to play again? (Y/y for yes, N/n for no.): ").strip().lower()
    if userinput == "y":
        user.clear
        cmp.clear
        return userinput
    else:
        if userinput != "n":
            print("Invalid input.")
        else:
            None

min1 = getvalidint(1)
max1 = getvalidint(2)
target1 = random.randint(min1, max1)
user = []
cmp = []

while True:
   userGuesses = playUserrounds(min1, max1, target1, user)
   compGuesses = playCMProunds(min1, max1, target1, cmp)
   printoutcome(userGuesses, compGuesses)
   if playagain() == "y":
       target = random.randint
   else:
        print("Have a good day!")
        break