"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

class Ugly:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 0
        j = 1
        while i < n:
            k = j
            while k % 2 == 0:
                k = k//2
            while k % 3 == 0:
                k = k//3
            while k % 5 == 0:
                k = k//5
                
            if k == 1:
                i += 1
            j += 1
            
        return j - 1