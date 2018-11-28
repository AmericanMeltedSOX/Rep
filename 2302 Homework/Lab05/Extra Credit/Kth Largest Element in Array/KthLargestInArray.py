"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

class KthLargestInArray:
    def kth_largest(self, array, k):
      # List to store indexes of greatest numbers
      great_index = []

      # Loops through array to find largest element until k is 0
      while k > 0:
        max_val = array[0]
        max_in = -1
        for i in range(len(array)):
          # Checks if element index is not in list
          if i not in great_index:
            # New max if element is greater than current max
            if array[i] > max_val:
              max_val = array[i]
              max_in = i

        #print(max_val)
        # Adds max value index to list
        great_index.append(max_in)
        k -= 1

      # returns elemnent that is kth largest
      return max_val


