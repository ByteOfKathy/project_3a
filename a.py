import os
print(os.getcwd()) # prints the working directory
import pandas as pd
from io import StringIO
foodData = pd.read_csv('foodDataCleaned.csv')
a = foodData.loc[[223572]] # position
productname = (a.values[0,0])
energy_100g = (a.values[0,1])
fat_100g = (a.values[0,2])
carbohydrates_100g = (a.values[0,3])
proteins_100g = (a.values[0,4])
ingredients_text = (a.values[0,5])

print('productname: ' +productname + '\n')
print('energy_100g: ' , energy_100g , '\n')
print('fat_100g: ' ,fat_100g , '\n')
print('carbohydrates_100g: ' , carbohydrates_100g , '\n')
print('proteins_100g: ' ,proteins_100g , '\n')
<<<<<<< HEAD
print('ingredients_text: ' + ingredients_text + '\n')
=======
print('ingredients_text: ' + ingredients_text + '\n')
>>>>>>> origin/ashley_branch
