""""
   test file for the hashTable
   I'm not really sure how to test properly, so I added
<<<<<<< HEAD
   all the values to to map and tested a couple of lookups. 
"""
import pandas as pd
import numpy as np
from hashTable import hashTable
def main():

    t = hashTable()
    foodData = pd.read_csv('foodDataCleaned.csv')
    b = foodData.values
    names = b[:,0]
    print(names)
    for i in b:
        t.insert(i)
    
    
=======
   all the values to to map and tested a couple of lookups.
"""
import pandas as pd
from hashTable import hashTable


def main():
    t = hashTable()
    foodData = pd.read_csv('food_data_no_duplicates.csv')
    b = foodData.values
    for i in b:
        t.insert(i)

>>>>>>> origin/ashley_branch
    print(t.getItem('Organic Medium Shredded Coconut'))
    print(t.getItem('Peanuts'))
    print(t.getItem('Organic White Basmati Rice')[4])
    print(t.getItem('Cakes aux Fruits')[2])
    print(t.size)
<<<<<<< HEAD
    #product names for searching
    foodData = pd.read_csv('foodDataCleaned.csv')
    productNames = foodData.loc[:,'product_name']
    #returns an array of productnames that match "steak"
=======
    # product names for searching
    productNames = foodData.loc[:, 'product_name']
    # returns an array of productnames that match "steak"
>>>>>>> origin/ashley_branch
    steak = search("steak", productNames)
    print(steak[5])
    "prints the products that match steak in the hashTable"
    for i in steak:
        print(t.getItem(i))

<<<<<<< HEAD
def search(userInput,productNames): 
    return(productNames[productNames.str.contains(userInput)].values)
    
    


main()
=======

def search(userInput, productNames):
    return (productNames[productNames.str.contains(userInput)].values)


main()
>>>>>>> origin/ashley_branch
