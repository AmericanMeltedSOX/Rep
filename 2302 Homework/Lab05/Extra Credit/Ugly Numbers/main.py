"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

from Ugly import Ugly

def main():
    x = Ugly()
    # Finds ugly number at 10th position
    f = x.nthUglyNumber(10)
    print("nth ugly number:", f)
    
main()
