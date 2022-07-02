# Mastermind CLI

### Overview
Mastermind CLI is a basic python script I’ve made to apply some of the basics I’ve learnt. Similar to how actual mastermind works the player must input their guess and then the amount of set and correct values is returned to them. Using whats returned to you each time you must guess the code.

## Rules
- Each number can only be from 1-8.
- You win once all 4 numbers are set.
- The code contains no duplicates so codes such as `1 2 2 8` `2 8 2 2` are impossible.
- You have 10 tries to crack the code before the game ends and you lose.
- At the end of the game the code is revealed to the player.

#### Guess handling

- Invalid guesses such as `1762`, `4 6 1 8 8`, `   ` will just return that the guess is invalid. 
- Guesses such as `1 1 1 1`, `a s d f`, `1 2 56 10000000000` are invalid but will just be treated as normal guesses. I may fix this but for now make sure your guess is valid before pressing enter.


### Example Game
```
Enter your guess (E.g: 1 2 3 4): 7 2 8 5
0 set, 2 correct but not set, 9 tries left.
```
