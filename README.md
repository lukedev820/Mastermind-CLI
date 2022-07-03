# Mastermind CLI

### Overview
Mastermind CLI is a basic python script I’ve made to apply some of the basics I’ve learnt. Similar to how actual mastermind works the player must input their guess and then the amount of set and correct values is returned to them. Using whats returned to you each time you must guess the code.
<br><br>

<p align="center">  
  <img width="772" src="https://github.com/lukedev820/Mastermind-CLI/blob/master/Example-game.png">
</p>
<br>

## Installation



1) Download the latest version of [Mastermind CLI](https://github.com/lukedev820/Mastermind-CLI) from this repository:
```
git clone https://github.com/lukedev820/Mastermind-CLI.git
cd Mastermind-CLI
```

2) Install the dependencies:
```
pip3 install random
```

<br><br>

## Rules
- Each number can only be from 1-8.
- You win once all 4 numbers are set.
- The code contains no duplicates so codes such as `1 2 2 8` `2 8 2 2` are impossible.
- You have 10 tries to crack the code before the game ends and you lose.
- At the end of the game the code is revealed to the player.

#### Guess handling

- Invalid guesses such as `1762`, `4 6 1 8 8`, `   ` will just return that the guess is invalid. 
- Guesses such as `1 1 1 1`, `a s d f`, `1 2 56 10000000000` are invalid but will just be treated as normal guesses. I may fix this but for now make sure your guess is valid before pressing enter.

