"""
CS 2302: LAB 7 Option A
From: ISAAC ACOSTA
DATE: 12/07/18
"""

class EditDistance:

    def edit_distance(str_1, str_2, m, n):

        print(str_1, str_2)
        # Creates a table to store results of subproblems
        d_p = [[0 for x in range(n+1)] for x in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):

                # If first string is empty, only option is to
                # insert all characters of second string
                if i == 0:
                    d_p[i][j] = j
                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0:
                    d_p[i][j] = i
                # If Characters are are the same, it ignores it.
                elif str_1[i-1] == str_2[j-1]:
                    d_p[i][j] = d_p[i-1][j-1]
                # Considers all possibilities
                else:
                    d_p[i][j] = 1 + min(d_p[i][j-1],    # Insert
                                        d_p[i-1][j],    # Remove
                                        d_p[i-1][j-1]   # Replace
                                        )

        return d_p[m][n]    # Returns distance
