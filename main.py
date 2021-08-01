import time

from hashTable import *
from BST import *

def search(userInput, productNames):
    return (productNames[productNames.str.contains(userInput)].values)

def sort(array, metric):
    array.sort(key=lambda x: x[metric])
    for i in array:
        print (i)


def main():
    foodData = pd.read_csv('food_data_no_duplicates.csv')
    b = foodData.values
    resultSort = []

    dataStructureChoice = 0
    while dataStructureChoice != 3:
        print ("Welcome to the nutrition look-up tool.")
        print ("Please select which data structure you would like to use:")
        print ("1. Map")
        print ("2. Tree")
        print ("Press 3 to quit.")

        dataStructureChoice = input()
        if dataStructureChoice == "3":
            break
        if dataStructureChoice == "1" or dataStructureChoice == "2":
            print ("Thank you! Please enter the item you are searching for:")

            item = input()

            # product names for searching
            productNames = foodData.loc[:, 'product_name']

            result = search(item, productNames)

            if dataStructureChoice == "1":
                start = time.time()
                t = hashTable()

                for i in b:
                    t.insert(i)

                #prints the products that match in the hashTable
                for i in result:
                    print(t.getItem(i))
                    resultSort.insert(0, t.getItem(i))
                end = time.time()
                print ("The time it took for this process is: ")
                print(end-start)

            elif dataStructureChoice == "2":
                start1 = time.time()
                tree = BST()
                for i in b:
                    tree.insertNode(i, tree.getRoot())

                for i in result:
                    print(tree.searchNode(i, tree.getRoot()))
                end1 = time.time()
                print("The time it took for this process is: ")
                print(end1 - start1)

            print("Which metric would you like to sort by?")
            print("1. Calories")
            print("2. Fat")
            print("3. Carbohydrates")
            print("4. Protein")

            sortingMetric = input()

            if sortingMetric == "1":
                sort(resultSort, 1)

            elif sortingMetric == "2":
                sort(resultSort, 2)

            elif sortingMetric == "3":
                sort(resultSort, 3)

            elif sortingMetric == "4":
                sort(resultSort, 4)

            else:
                print("I'm sorry. That is not a valid option.")
        else:
            print("I'm sorry. That is not a valid choice.")



main()


