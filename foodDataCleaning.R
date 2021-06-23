#Group 9  Ashley Bellomy, Justin Broce, Katherine Chan
#Professor Amanpreet Kapoor
#COP 3530 Data structures and Algorithms
#Data Cleaning
library(tidyverse)
# Data downloaded from https://www.kaggle.com/openfoodfacts/world-food-facts
foodData <- read_tsv("en.openfoodfacts.org.products.tsv")
foodData <- foodData %>% 
  #selecting the columns of data we want...
  select(product_name, energy_100g, fat_100g, carbohydrates_100g,proteins_100g,ingredients_text) %>% 
  #removing NAs
  filter(
    !is.na(product_name),
    !is.na(ingredients_text),
    !is.na(energy_100g),
    !is.na(fat_100g),
    !is.na(carbohydrates_100g),
    !is.na(proteins_100g)
  )
#exporting the dataframe to csv
write_csv(foodData,path = "foodDataCleaned.csv")

