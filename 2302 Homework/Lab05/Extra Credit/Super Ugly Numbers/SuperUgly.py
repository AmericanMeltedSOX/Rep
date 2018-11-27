"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

class SuperUgly:
    def nth_Super_Ugly_Number(self, n, primes):

        i = 0
        j = 1
        while i < n:
          k = j
          # Calculates super ugly number
          for p in range(len(primes)):
            # Goes through every elemet of list 'primes'
            while k % primes[p] == 0:
              k = k // primes[p]
          # Checks if it is super ugly number
          if k == 1:
            i += 1
          j += 1

        # returns super ugly number at nth position
        return j - 1
