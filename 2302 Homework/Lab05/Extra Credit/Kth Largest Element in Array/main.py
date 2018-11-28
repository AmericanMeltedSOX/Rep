"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

from KthLargestInArray import KthLargestInArray

def main():
    x = KthLargestInArray()

    # Array of integers to find the largest element
    array = [3,2,3,1,2,4,5,5,6]
    k = 4

    # Calculate number that is kth largest
    f = x.kth_largest(array, k)
    print("Kth element:", f)
    
main()