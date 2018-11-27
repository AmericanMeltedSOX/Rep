class Heap:

  def __init__(self):
    self.heap_array = []


  def insert(self, k):
    # add the new value to the end of the array.
    self.heap_array.append(k)

    # percolate up from the last index to restore heap property.
    self.percolate_up(len(self.heap_array) - 1)

  # Removes min element and returns it
  def extract_min(self):
    # Check if heap is empty
    if self.is_empty():
      return
    # save the min value from the root of the heap.
    min_element = self.heap_array[0]

    # move the last item in the array into index 0.
    replace_value = self.heap_array.pop()
    if len(self.heap_array) > 0:
      self.heap_array[0] = replace_value

      # percolate down to restore min heap property.
      self.percolate_down(0, len(self.heap_array))

    # return min value
    return min_element

  # Heapsort function
  def heap_sort(self):
    # Heapify number list
    i = len(self.heap_array) // 2
    while i > 0:
      self.percolate_down(i, len(self.heap_array))
      i -= 1

    i = len(self.heap_array) - 1
    while i > 0:
      # Swap numbers[0] and numbers[i]
      temp = self.heap_array[0]
      self.heap_array[0] = self.heap_array[i]
      self.heap_array[i] = temp

      self.percolate_down(0, i)
      i -= 1
    
    # Reverse the heap list from least to greatest value
    self.heap_array.reverse()


  # Percolate up function
  def percolate_up(self, node_index):
    # start a last index.
    while node_index > 0:
      # compute the parent node's index
      parent_index = (node_index - 1)//2

      # check for a violation of the min heap property
      if self.heap_array[node_index] >= self.heap_array[parent_index]:
        # no violation, so percolate up is done.
        return
      else:
        # swap heap_array[node_index] and heap_array[parent_index]
        temp = self.heap_array[node_index]
        self.heap_array[node_index] = self.heap_array[parent_index]
        self.heap_array[parent_index] = temp

        # continue the loop from the parent node
        node_index = parent_index

  # Percolate down function
  def percolate_down(self, node_index, size):
    # Computes the child of node's index
    child_index = 2 * node_index + 1
    value = self.heap_array[node_index]

    while child_index < size:
      # Find the min among the node and the node's children
      min_value = value
      min_index = -1
      i = 0
      while (i < 2) and (i + child_index < len(self.heap_array)):
        if self.heap_array[i + child_index] < min_value:
          min_value = self.heap_array[i + child_index]
          min_index = i + child_index
        i += 1

      # check for a violation of the min heap property
      if min_value == value:
        return
      else:
        # swap heap_array[node_index] and heap_array[max_index]
        temp = self.heap_array[node_index]
        self.heap_array[node_index] = self.heap_array[min_index]
        self.heap_array[min_index] = temp

        # continue loop from the smaller child node
        node_index = min_index
        child_index = 2 * node_index + 1

    
  def is_empty(self):
    return len(self.heap_array) == 0

  def printer(self):
    for i in range(len(self.heap_array)):
      print(self.heap_array[i])