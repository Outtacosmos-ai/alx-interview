# Prime Game

## Description

**Prime Game** is a Python script that determines the winner of a game played by two players, Maria and Ben. The game involves selecting prime numbers from a set of integers and removing the selected primes along with their multiples. The player unable to make a move loses. The program computes the winner after multiple rounds of the game.

## Requirements

- **Python version:** 3.4.3
- **Operating System:** Ubuntu 20.04 LTS
- Code must conform to **PEP 8 style guidelines**.
- No external libraries or packages are allowed.

## Usage

Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-interview.git
   cd alx-interview/0x0A-primegame

Function prototye:
def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    - x: (int) The number of rounds.
    - nums: (list) List of integers representing the maximum number in each round.

    Returns:
    - (str) Name of the player who won the most rounds, or None if no winner.
    """

Input:
x = 3
nums = [4, 5, 1]


Output:
Winner: Ben


Structure:
0x0A-primegame/
│
├── 0-prime_game.py  # Implementation of the prime game logic
├── main_0.py        # Example main file for testing
├── README.md        # Project documentation

Style guide:
pycodestyle 0-prime_game.py


Author:
Mohamed ESSRHIR AKA Outtacosmos-ai
