import numpy as np
import pandas as pd


class hashTable:
    # capacity is number of items
    def __init__(self, capacity=500000):
        # Create a numpy array full of Not avaibles
        self.table = np.full((capacity), np.nan, object)
        self.size = 0
        self.capacity = capacity

    # get item of the repective key
    def getItem(self, key):
        pos = self.findPos(key)
        return self.table[pos]

    def hash(self, key):
        hashVal = 0
        for ch in key:
            hashVal = 37 * hashVal + ord(ch)
        return hashVal % self.capacity

    """findPos function inspired by the weiss textbook
    finds the index of the given key, or if key doesn't exit returns an empty index
    """

    def findPos(self, key):
        offset = 1
        currentPos = self.hash(key)
        while np.size(self.table[currentPos]) == 6 and \
                key != self.table[currentPos][0]:
            currentPos += offset
            offset += 2

            if currentPos >= self.capacity:
                currentPos -= self.capacity
        return currentPos

    def insert(self, item):
        currentPos = self.findPos(item[0])
        if np.size(self.table[currentPos]) != 6:
            self.table[currentPos] = item[:]
            self.size += 1