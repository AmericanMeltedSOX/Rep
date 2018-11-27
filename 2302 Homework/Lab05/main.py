"""
CS 2302
Assignment: LAB 5 Option A
From: ISAAC ACOSTA
DATE: 11/27/18
"""

from Heap import Heap
import time

def main():

  start_time = time.time() # Starts time
  read_file() # Calls the function to read the text file
  end_time = time.time()
  
  # Prints running time.
  print("Total Running time:", end_time - start_time)

# Reads text file
def read_file():
  text_file = open('text.txt', 'r')

  # Reads first line
  for line in text_file:
    # For every line, it seperates by comma and casts the integer elements
    curr_line = line.split(",") 

  min_heap = Heap() # Initializes min-heap object from Heap Class

  # Gets all elements from curr_line list and inserts into the heap.
  for i in range(len(curr_line)):
    min_heap.insert(int(curr_line[i]))

  print("First insertions list:")
  min_heap.printer()  # Prints first list after insertion process

  print() # Prints the min elemet from extract_min() from Heap class
  print("Extract min return element:", min_heap.extract_min())
  print()
  
  # Prints list after removal
  print("List after removal:")
  min_heap.printer()
  print()

  print("List after proper Heapsort:")
  min_heap.heap_sort()
  min_heap.printer()  # Prints list after proper Heapsort

  

main()