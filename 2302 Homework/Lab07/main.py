"""
CS 2302: LAB 7 Option A
From: ISAAC ACOSTA
DATE: 12/07/18
"""

from EditDistance import EditDistance
import time

def main():

    start_time = time.time()
    # Hardcoded test 1
    str_1 = "help"
    str_2 = "heap"
    e_d = EditDistance.edit_distance(str_1, str_2, len(str_1), len(str_2))
    print("Test 1:", e_d)
    end_time = time.time()
    print("Running Time:", end_time - start_time)
    print()

    # Hardcoded test 2
    start_time = time.time()
    str_1 = "MONKEY"
    str_2 = "MONEY"
    e_d = EditDistance.edit_distance(str_1, str_2, len(str_1), len(str_2))
    print( "Test 2:", e_d)
    print("Running Time:", end_time - start_time)
    print()

    # Hardcoded test 3
    start_time = time.time()
    str_1 = "Saturday"
    str_2 = "Sunday"
    e_d = e_d = EditDistance.edit_distance(str_1, str_2, len(str_1), len(str_2))
    print("Test 3:", e_d)
    end_time = time.time()
    print("Running Time:", end_time - start_time)
    print()

    # Hardcoded test 3
    start_time = time.time()
    str_1 = "synonym"
    str_2 = "systems"
    e_d = EditDistance.edit_distance(str_1, str_2, len(str_1), len(str_2))
    print("Test 4", e_d)
    end_time = time.time()
    print("Running Time:", end_time - start_time)




main()

