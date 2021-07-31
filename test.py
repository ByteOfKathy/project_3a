from numpy import product
import BST
import node
import pandas as pd

df = pd.read_csv("foodDataCleaned.csv")
testArr = []

# uncomment this for testing the node class 
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

assert node.isSame(test1, testArr[0]), "test 1 failed"
assert node.isSame(test2, testArr[1]), "test 2 failed"
assert node.isSame(test3, testArr[2]), "test 3 failed"
assert node.isSame(test4, testArr[3]), "test 4 failed"
print("Node tests passed")