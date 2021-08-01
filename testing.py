""""
   test file for the hashTable
   I'm not really sure how to test properly, so I added
   all the values to to map and tested a couple of lookups. 
"""
import pandas as pd
from hashTable import hashTable
def main():
    t = hashTable()
    foodData = pd.read_csv('foodDataCleaned.csv')
    b = foodData.values
    for i in b:
        t.insert(i)
    
    
    print(t.getItem('Organic Medium Shredded Coconut'))
    print(t.getItem('Peanuts'))
    print(t.getItem('Organic White Basmati Rice')[4])
    print(t.getItem('Cakes aux Fruits')[2])
    print(t.size)
main()