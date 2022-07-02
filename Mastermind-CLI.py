import random #Importing the random library to make use of its random numbers.


#Play function
def play():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8'] #Numbers the code can be made of.
    code = random.sample(numbers, 4) #Creates the code by randomly picking 4 values from numbers

    #Setting game values
    tries = 10 #Amount of tries the player has.
    set = 0 #How many numbers are correct and in the right position 
    correct = 0 #How many numbers are correct but not in the right position. 
    codeBroken = False #Have all the numbers been set.

    while tries > 0: #While the users tries is above 0.
        try:
            guess = input("Enter your guess (E.g: 1 2 3 4): ").split() #Allow the user to enter a code.

            for i, number in enumerate(guess):
                if code[i] == guess[i]:
                    set += 1
                elif number in code:
                    correct += 1

            if set == len(code): #if all numbers have been set 
                codeBroken = True
                break
            tries -= 1 #Once the guess has succesfully been made take a try off.
            print(f"{set} set, {correct} correct but not set, {tries} tries left.") #Print the current status of the code.
            correct, set = 0, 0 #Reset the checks for the next guess.
        
        except:
            print("Invalid Guess")
            
    print("The code was:", code) #Once the game is over print the code.
    if codeBroken == True:
        print ("You win!")
    else: 
        print("You couldnt crack the code!")

if __name__ == '__main__':
    play()
