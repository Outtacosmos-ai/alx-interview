#!/usr/bin/python3

def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(n):
    """Generate a list of prime numbers up to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Maria and Ben take turns choosing primes. The player who cannot make
    a move loses the round.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        turn = 0  # Maria starts first
        while primes:
            turn += 1
            # Remove a prime and all its multiples
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
