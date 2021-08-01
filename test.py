from numpy import product
import BST
import node
import pandas as pd

df = pd.read_csv("foodDataCleaned.csv")
    
# hard coded test nodes
test1 = node.Node(
    product = "Banana Chips Sweetened (Whole)", 
    energy = 2243.0, 
    fat = 28.57, 
    carbs = 64.29, 
    proteins = 3.57, 
    ingredients = "Bananas, vegetable oil (coconut oil, corn oil and/or palm oil) sugar, natural banana flavor."
)

test2 = node.Node(
    product = "Peanuts", 
    energy = 1941.0, 
    fat = 17.86, 
    carbs = 60.71, 
    proteins = 17.86, 
    ingredients = "Peanuts, wheat flour, sugar, rice flour, tapioca starch, salt, leavening (ammonium bicarbonate, baking soda), soy sauce (water, soybeans, wheat, salt), potato starch."
)

test3 = node.Node(
    product = "Organic Salted Nut Mix", 
    energy = 2540.0, 
    fat = 57.14, 
    carbs = 17.86, 
    proteins = 17.86, 
    ingredients = "Organic hazelnuts, organic cashews, organic walnuts almonds, organic sunflower oil, sea salt."
)

test4 = node.Node(
    product = "Organic Polenta", 
    energy = 1552.0, 
    fat = 1.43, 
    carbs = 77.14, 
    proteins = 8.57, 
    ingredients = "Organic polenta"
)

# uncomment this for testing the node class 
print("- starting node tests...\n")

testArr = []

for i in range(4):
    n = node.Node(
        df["product_name"][i],
        df["energy_100g"][i],
        df["fat_100g"][i],
        df["carbohydrates_100g"][i],
        df["proteins_100g"][i],
        df["ingredients_text"][i]
    )
    testArr.append(n)

# assertions
print("testing first 4 nodes from csv sheet vs. hard coded nodes...")
assert node.isSame(test1, testArr[0]), "test 1 failed"
assert node.isSame(test2, testArr[1]), "test 2 failed"
assert node.isSame(test3, testArr[2]), "test 3 failed"
assert node.isSame(test4, testArr[3]), "test 4 failed"
print("Node tests passed\n")

# uncomment this to test BST methods
print("- starting BST tests...\n")
bstSoln = BST.BST(test3)

# sorting by product name
test3.right = test2
test2.parent = test3

test3.left = test1
test1.parent = test3

# bstSoln.printInOrder(bstSoln.getRoot())

test1BST = node.Node(
    product = "Banana Chips Sweetened (Whole)", 
    energy = 2243.0, 
    fat = 28.57, 
    carbs = 64.29, 
    proteins = 3.57, 
    ingredients = "Bananas, vegetable oil (coconut oil, corn oil and/or palm oil) sugar, natural banana flavor."
)

test2BST = node.Node(
    product = "Peanuts", 
    energy = 1941.0, 
    fat = 17.86, 
    carbs = 60.71, 
    proteins = 17.86, 
    ingredients = "Peanuts, wheat flour, sugar, rice flour, tapioca starch, salt, leavening (ammonium bicarbonate, baking soda), soy sauce (water, soybeans, wheat, salt), potato starch."
)

test3BST = node.Node(
    product = "Organic Salted Nut Mix", 
    energy = 2540.0, 
    fat = 57.14, 
    carbs = 17.86, 
    proteins = 17.86, 
    ingredients = "Organic hazelnuts, organic cashews, organic walnuts almonds, organic sunflower oil, sea salt."
)

bstTest = BST.BST(test3BST)
bstTest.insertNode(test2BST, bstTest.getRoot())
bstTest.insertNode(test1BST, bstTest.getRoot())

try:
    bstTest.insertNode(test3BST, bstTest.getRoot())
    print("duplicate test failed, did you forget to uncomment the value error in BST.py?")
    raise AssertionError
except ValueError:
    print("duplicate test passed")

# bstTest.printInOrder(bstTest.getRoot())

# assertions
print("testing BST insertNode using first 3 nodes from csv sheet vs. hard coded nodes...")
assert node.isSame(bstSoln.getRoot(), bstTest.getRoot()), "test 1 failed"
assert node.isSame(bstSoln.getRoot().left, bstTest.getRoot().left), "test 2 failed"
assert node.isSame(bstSoln.getRoot().right, bstTest.getRoot().right), "test 3 failed"

assert bstSoln.getRoot().parent == bstTest.getRoot().parent, "test 4 failed"
assert node.isSame(bstSoln.getRoot().left.parent, bstTest.getRoot().left.parent), "test 5 failed"
assert node.isSame(bstSoln.getRoot().right.parent, bstTest.getRoot().right.parent), "test 6 failed"

print("testing BST searchNode (node)...")
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot(), bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot(), bstTest.getRoot())), "test 7 failed"
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot().left, bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot().left, bstTest.getRoot())), "test 8 failed"
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot().right, bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot().right, bstTest.getRoot())), "test 9 failed"
assert bstTest.searchNode(test4, bstTest.getRoot()) is None, "test 10 failed"

print("testing BST searchNode (string)...")
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot().getProduct(), bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot().getProduct(), bstTest.getRoot())), "test 11 failed"
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot().left.getProduct(), bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot().left.getProduct(), bstTest.getRoot())), "test 12 failed"
assert node.isSame(bstSoln.searchNode(bstSoln.getRoot().right.getProduct(), bstSoln.getRoot()), bstTest.searchNode(bstTest.getRoot().right.getProduct(), bstTest.getRoot())), "test 13 failed"
assert bstTest.searchNode(test4.getProduct(), bstTest.getRoot()) is None, "test 14 failed"

print("BST tests passed\n")