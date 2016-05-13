# Implementation of minheap.
# The heap is an array which has the property that indices 2i and 2i + 1 are
# elements in the array which are greater than the element at index i.

# Operations:
# min_heapify
# build_min_heap
# insert
# delete
# Since finding an element is O(n), it is just an array search.

# Implementation
# A list will be used to implement this.
# zero-indexing will be used. So i corresponds to 2i + 1 and 2i + 2.
# min_heapify assumes that the subheaps at i's children are already heaps, and
# makes the heap rooted at i also a heap

# build_min_heap just uses min_heapify n/2 times.

# insert will insert at end of heap, and in O(lgn) re-heapify the heap.

# delete will swap with the last element, and then pop the list. Then, the
# element has to be moved up OR down until the heap property is satisfied. At
# that moment, the list is a minheap. This is O(lgn)

import unittest
import heapq

class TestHeap(unittest.TestCase):
    def initialize(self):
        self.array = [
            73, 88, 1, 4, 54, 72, 34, 95, 18, 94, 27, 8, 69, 47, 18, 45, 99,
            66, 90, 26, 17, 38, 36, 6, 57, 15, 99, 47, 5, 40, 58, 95, 43, 30,
            93, 53, 33, 63, 41, 92, 80, 42, 47, 43, 46, 15, 23, 13, 89, 97, 22,
            96, 76, 10, 82, 21, 34, 1, 34, 67, 58, 3, 29, 86, 32, 36, 0, 71,
            54, 89, 39, 22, 57, 75, 58, 60, 11, 73, 7, 98, 45, 70, 3, 63, 67,
            24, 59, 59, 89, 78, 45, 85, 65, 74, 84, 62, 97, 51, 80, 76]
        self.arraylen = 100
        self.heap = Heap(self.array)

    def check_heap(self):
        for i in range(self.heap.len() / 2):
            node = self.heap.array[i]
            parent_index = (i - 1) / 2
            parent_exists = i != 0
            left_child_index = 2 * i + 1
            left_child_exists = left_child_index < self.heap.len()
            right_child_index = 2 * i + 2
            right_child_exists = right_child_index < self.heap.len()
            if parent_exists and not self.heap.array[parent_index] <= node:
                return False
            if (left_child_exists and not self.heap.array[left_child_index] >=
                node):
                return False
            if (right_child_exists and not self.heap.array[right_child_index] >=
                node):
                return False
        return True

    def test_test(self):
        self.initialize()
        heapq.heapify(self.array)
        self.assertTrue(self.check_heap())

    def test_min_heapify(self):
        self.initialize()
        heapq.heapify(self.array)

        self.array[0] = 50
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 100
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 987
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 0
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = -40
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 20
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 97
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 29
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 49
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 78
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())
        self.array[0] = 41
        self.heap.min_heapify(0)
        self.assertTrue(self.check_heap())

    def test_build_min_heap(self):
        self.initialize()
        self.heap.build_min_heap()
        self.assertTrue(self.check_heap())

    def test_insert(self):
        self.initialize()
        heapq.heapify(self.array)
        self.heap.insert(100)
        self.assertTrue(self.check_heap())
        self.heap.insert(50)
        self.assertTrue(self.check_heap())
        self.heap.insert(29)
        self.assertTrue(self.check_heap())
        self.heap.insert(27)
        self.assertTrue(self.check_heap())
        self.heap.insert(69)
        self.assertTrue(self.check_heap())
        self.heap.insert(47)
        self.assertTrue(self.check_heap())
        self.heap.insert(0)
        self.assertTrue(self.check_heap())
        self.heap.insert(94)
        self.assertTrue(self.check_heap())
        self.heap.insert(10)
        self.assertTrue(self.check_heap())
        self.heap.insert(3)
        self.assertTrue(self.check_heap())
        self.heap.insert(93)
        self.assertTrue(self.check_heap())

    def test_delete(self):
        self.initialize()
        heapq.heapify(self.array)
        self.heap.delete(99)
        self.assertTrue(self.check_heap())
        self.heap.delete(50)
        self.assertTrue(self.check_heap())
        self.heap.delete(94)
        self.assertTrue(self.check_heap())
        self.heap.delete(27)
        self.assertTrue(self.check_heap())
        self.heap.delete(69)
        self.assertTrue(self.check_heap())
        self.heap.delete(47)
        self.assertTrue(self.check_heap())
        self.heap.delete(0)
        self.assertTrue(self.check_heap())
        self.heap.delete(29)
        self.assertTrue(self.check_heap())
        self.heap.delete(10)
        self.assertTrue(self.check_heap())
        self.heap.delete(3)
        self.assertTrue(self.check_heap())
        self.heap.delete(93)
        self.assertTrue(self.check_heap())
        self.heap.delete(50)
        self.assertTrue(self.check_heap())

class Heap(object):
    def __init__(self, l):
        """Using a list, initialize a heap object."""
        self.array = l

    def len(self):
        return len(self.array)

    def min_heapify(self, i):
        """min-heapify at 0-indexed i."""
        # Continue swapping if it has left and right children.
        while 2 * i + 2 < len(self.array):
            node = self.array[i]
            left_child = self.array[2*i + 1]
            right_child = self.array[2*i + 2]
            if node <= left_child and node <= right_child:
                # When this break is executed, the heap rooted at the original
                # ith element is verified as a heap.
                break
            elif right_child <= left_child:
                self.array[i], self.array[2 * i + 2] = right_child, node
                i = 2 * i + 2
            else:
                self.array[i], self.array[2 * i + 1] = left_child, node
                i = 2 * i + 1
        # If its position has not been verified with the break being executed,
        # and it does not have left AND right children anymore, check if left
        # child exists and if the left child should be swapped with it. If it
        # does not have a left child, then as a leaf it already satifies the
        # heap invariant, and if both are true, then swapping it confirms its
        # place in the heap, since it will be a leaf after the swapping
        # operation.
        else:
            if (2 * i + 1 < len(self.array) and self.array[2 * i + 1] <
                self.array[i]):
                self.array[i], self.array[2 * i + 1] = (
                    self.array[2 * i + 1], self.array[i])

    def build_min_heap(self):
        for i in reversed(xrange((self.len() - 2) / 2 + 1)):
            self.min_heapify(i)

    def insert(self, e):
        """Insert element e into the heap while maintaining the heap."""
        self.array.append(e)
        i = len(self.array) - 1
        while i != 0 and self.array[(i - 1) / 2] > e:
            self.array[(i - 1) / 2], self.array[i] = e, self.array[(i - 1) / 2]
            i = (i - 1) / 2

    def delete(self, i):
        if i >= len(self.array):
            return None
        if i == len(self.array) - 1:
            return self.array.pop()
        self.array[i], self.array[-1] = self.array[-1], self.array[i]
        ret = self.array.pop()

        if i != 0 and self.array[(i - 1) / 2] > self.array[i]:
            while i != 0 and self.array[(i - 1) / 2] > self.array[i]:
                self.array[(i - 1) / 2], self.array[i] = self.array[i], self.array[(i - 1) / 2]
                i = (i - 1) / 2
        else:
            self.min_heapify(i)

        return ret

unittest.main()
