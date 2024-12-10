#!/usr/bin/python3
"""Solve the Prime Game problem where Maria and Ben take turns removing prime
numbers and their multiples from a set of numbers."""


def isPrime(n):
    """Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    # 1 and less are not prime
    if n <= 1:
        return False

    # Check for divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def findPrimes(n):
    """Find all prime numbers less than or equal to n.

    Args:
        n (int): Upper limit to find primes

    Returns:
        list: List of prime numbers
    """
    return [num for num in range(2, n + 1) if isPrime(num)]


def isWinner(x, nums):
    """Determine the winner of the Prime Game for multiple rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player with most wins, or None
    """
    # Handle invalid or empty inputs
    if not nums or x <= 0:
        return None

    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        # Find all primes for this round
        primes = findPrimes(n)

        # If no primes, Ben wins (Maria can't move first)
        if not primes:
            ben_wins += 1
            continue

        # Track available primes in this round
        available_primes = set(primes)
        current_player = 'Maria'

        # Simulate the game
        while available_primes:
            # Find the smallest prime
            prime = min(available_primes)

            # Remove this prime and its multiples
            available_primes = {
                p for p in available_primes
                if p % prime != 0
            }

            # Switch players
            current_player = 'Ben' if current_player == 'Maria' else 'Maria'

        # Last player who could move wins
        if current_player == 'Ben':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'

    return None
