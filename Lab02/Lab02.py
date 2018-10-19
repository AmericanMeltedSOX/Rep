"""CS 2302
Submitted and Modified by: ISAAC ACOSTA
Instructor: Aguirre, Diego
Date: 08/18/18
Assignment: Lab 02"""

import time

class Node:
    def __init__(self, password):
        self.password = password
        self.count = 1
        self.next = None

    def get_data(self):
        return self.password

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count

    def add_count(self):
        self.count += 1

class LinkedList:

    def __init__(self):
            #Constructor
        self.head = None
        self.tail = None

    def insert(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    def length(self):
        count = 0
        curr = self.head
        while curr is not None:
            count = count + 1
            curr = curr.next

        return count

    def output_list(self, x):
        """For value x, use any digit greater than 0 to output the top x
        passwords used, and x  = -1 will output every node in the linked list"""
        curr = self.head
        n = 0
        while curr is not None:

            if x > 0:
                if n == 0:
                    print("Top", x, "used passwords:")
                print(n+1, ":", curr.get_data(), "REPEATS:", curr.get_count())
                x -= 1
                n += 1
            elif x is -1:
                print(n+1, ":", curr.get_data())
                n += 1
            else:
                return

            curr = curr.next
        return

    def search(self, item):
        curr = self.head
        while curr is not None:
            if item == curr.get_data():
                curr.add_count()
                return 1
            else:
                curr = curr.next

        return 0

####     MERGE SORT      ####
    def split_list(self):
        x = self.length()

        left = LinkedList()
        right = LinkedList()
        curr = self.head

        for i in range(x//2):
            temp = Node(curr.get_data())
            temp.set_count(curr.get_count())
            left.insert(temp)
            curr = curr.next

        right.head = curr
        return left, right


    def mergeSortLinkedList(self):
        if self.head is None or self.head.next is None:
            return
        #Splits the list into two lists.
        left, right = self.split_list()

        left.mergeSortLinkedList()
        right.mergeSortLinkedList()

        self.merge_sort(left, right)

    def merge_sort(self, left, right):
        temp = LinkedList()
        #Merge sort algorithm
        while left.length()>0 and right.length()>0:
            if left.head.get_count() > right.head.get_count():
                temp.insert(left.head)
                left.head = left.head.next
            else:
                temp.insert(right.head)
                right.head = right.head.next

        while left.length() > 0:
            temp.insert(left.head)
            left.head = left.head.next

        while right.length() > 0:
            temp.insert(right.head)
            right.head = right.head.next
        #returns sorted list
        self.head = temp.head

###      BUBBLE SORT      ###
    def bubbleSortLinkedList(self):
        x = self.length()

        for i in range(x-1):
            curr = self.head
            self.head = None
            for j in range(x-1):
                if curr.next != None and curr.get_count() < curr.next.get_count():
                    temp = curr.next
                    curr.next = curr.next.next
                    temp.next = None
                else:
                    temp = curr
                    curr = curr.next
                    temp.next = None

                self.insert(temp) #Inserts new Node into list after bubble sort



def main():
    text_file()

    start_time = time.time()
    list_A = solution_A()
    end_time = time.time()
    print("Solution A Runnintg time: ", end_time - start_time)

    start_time = time.time()
    list_B = solution_B()
    end_time = time.time()
    print("Solution B Runnintg time: ", end_time - start_time)
    print()

    print("List A")
    list_A.output_list(20)

    print()

    print("List B")
    list_B.output_list(20)


def solution_A():
    file = open("passwords.txt", "r")
    a_list = LinkedList()

    for line in file:
        if a_list.search(line)== 0:
            temp = Node(line)
            a_list.insert(temp)

    a_list.bubbleSortLinkedList()
    return a_list

def solution_B():
    file = open("passwords.txt", "r")
    dict = {} #Dictionary Hash
    a_list = LinkedList()

    for line in file:
        if line in dict:
            dict[line].add_count()
        else:
            dict[line] = Node(line)

    for k, v in dict.items():
        a_list.insert(v)

    a_list.mergeSortLinkedList()
    return a_list

#Creates new text file after seperating and gathering the desired contents
def text_file():
    read = open("list.txt", "r")
    file = open("passwords.txt", "w")

    for line in read:
        lim = line.split("	")
        if len(lim) == 2:
            file.write(lim[1])


main()
