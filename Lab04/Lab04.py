"""
CS 2302: LAB 4 Option B
From: ISAAC ACOSTA
DATE: 11/11/18
"""


import time
# Hash table node
class Hash_node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Chaining Hash Table
class Chaining_hash_table:
    def __init__(self, table_size):
        self.table = [None] * table_size



    def hash(self, key):
        return key % len(self.table)

    # Insert to Hash table
    def insert(self, key):
        n = self.string_to_base10_integer(key) # n is to get integer to make modulo calculation
        loc = self.hash(n)

        if self.table[loc] is None: # If hash is none, initialize first Node
            self.table[loc] = Hash_node(key, None)
        else:                   # Create next Node
            temp = self.table[loc]
            self.table[loc] = Hash_node(key, temp)

    # Search for key word
    def search(self, key):

        n = self.string_to_base10_integer(key) # n is to make modulo calculation
        loc = self.hash(n)

        temp = self.table[loc]  # temp becomes hash index

        # If temp.item equals key, then temp.item is returned
        # else, none is returned
        while temp is not None:
            if temp.item.lower() == key.lower():
                return temp.item

            temp = temp.next

        return None

    # Load Factor
    def get_load_factor(self):

        num_elements = 0
        # Goes through each Hash index
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None: # Adds one until hash node in index is None
                num_elements += 1
                temp = temp.next

        # Number of elements divided by length of Hash table
        return num_elements / len(self.table)


    # Converts string to an integer
    # EX. A = 0 Z = 25
    def string_to_base10_integer(self, word):

        A_UPPERCASE = ord('A')
        ALPHABET_SIZE = 26

        return -1 + sum(    # Returns a number that can be sed to make modulo
            (ord(letter) - A_UPPERCASE + 1) * ALPHABET_SIZE**i
            for i, letter in enumerate(reversed(word.upper()))
        )


def main():

    # Reads text file words.txt
    file = open('words.txt', 'r')
    table_size = 512

    start_time = time.time()    # Gets running time for Hash table operations
    engish_words = populate_hash(file, table_size)
    end_time = time.time()
    print("Creation of hash table running time:", end_time - start_time)    # Prints running time to create Hash Table


    start_time = time.time()    # Gets time to retrieve a string from table
    print(engish_words.search("blue"))
    end_time = time.time()
    print("Retrieval of word, running time:", end_time - start_time) # Prints running time to retrieve from hash table


    start_time = time.time()    # Finds running time for find_anagrams algorithm
    print(num_of_anagrams("spot", engish_words, 0, ""))
    end_time = time.time()
    print("Find anagrams algorithm running time:", end_time - start_time)   # Prints running time for finding anagrams

    print("Hash table load factor for length", table_size, ":")
    print( engish_words.get_load_factor() )                      # Returns load factor


# Populates hash table and gets table_size as reference
def populate_hash(file, table_size):
    hash_table = Chaining_hash_table(table_size)

    for line in file:   # For each line, it is added to hash table
        line = line.rstrip('\n')    # Line is converted to proper string
        hash_table.insert(line)

    file.close()    # Returns hash table
    return hash_table

# Get Number of anagrams for a String
def num_of_anagrams(word, hash_table, n, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        find_anagram = hash_table.search(str)
        if find_anagram is not None:
            print(find_anagram)
            n+=1    # Adds one if string is found in the hash table

    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur

            if cur not in before: # Check if permutations of cur have not been generated.
                n += num_of_anagrams(before + after, hash_table, 0, prefix + cur) # Recusively returns all anagrams found in hash table
    # Returns number of Anagrams
    return n


main()
