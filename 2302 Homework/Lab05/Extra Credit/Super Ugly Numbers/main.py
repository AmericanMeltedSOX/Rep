"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

from SuperUgly import SuperUgly

def main():
    x = SuperUgly()

    # List of prime numbers
    primes = [2, 7, 13, 19]
    # To fetch super ugly number at 12th position
    f = x.nth_Super_Ugly_Number(12, primes)
    print("nth super ugly number:", f)
    
main()