import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori

# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
# shape为(7501,20)
#print(dataset.shape)
# 将数据存放到transactions中
transactions = []
# 遍历整个表转化为数组
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.4)
print("频繁项集：", itemsets)
print("关联规则：", rules)
"""Result"""
#频繁项集： {1: {('low fat yogurt',): 574, ('salmon',): 319, ('avocado',): 250, ('mineral water',): 1788, ('almonds',): 153, ('frozen smoothie',): 475, ('shrimp',): 536, ('energy drink',): 200, ('tomato juice',): 228, ('vegetables mix',): 193, ('cottage cheese',): 239, ('olive oil',): 494, ('green tea',): 991, ('honey',): 356, ('eggs',): 1348, ('burgers',): 654, ('meatballs',): 157, ('turkey',): 469, ('whole wheat rice',): 439, ('energy bar',): 203, ('milk',): 972, ('french fries',): 1282, ('whole wheat pasta',): 221, ('soup',): 379, ('spaghetti',): 1306, ('frozen vegetables',): 715, ('cookies',): 603, ('cooking oil',): 383, ('champagne',): 351, ('chocolate',): 1229, ('chicken',): 450, ('oil',): 173, ('fresh tuna',): 167, ('tomatoes',): 513, ('red wine',): 211, ('pepper',): 199, ('pancakes',): 713, ('ham',): 199, ('grated cheese',): 393, ('fresh bread',): 323, ('ground beef',): 737, ('escalope',): 595, ('herb & pepper',): 371, ('strawberries',): 160, ('cake',): 608, ('hot dogs',): 243, ('brownies',): 253, ('cereals',): 193, ('muffins',): 181, ('light mayo',): 204, ('yogurt cake',): 205, ('butter',): 226, ('french wine',): 169}, 2: {('frozen smoothie', 'mineral water'): 152, ('green tea', 'mineral water'): 233, ('low fat yogurt', 'mineral water'): 180, ('mineral water', 'olive oil'): 207, ('mineral water', 'shrimp'): 177, ('burgers', 'eggs'): 216, ('milk', 'mineral water'): 360, ('mineral water', 'whole wheat rice'): 151, ('frozen vegetables', 'spaghetti'): 209, ('green tea', 'spaghetti'): 199, ('burgers', 'mineral water'): 183, ('cooking oil', 'mineral water'): 151, ('eggs', 'mineral water'): 382, ('chicken', 'mineral water'): 171, ('eggs', 'spaghetti'): 274, ('mineral water', 'spaghetti'): 448, ('mineral water', 'tomatoes'): 183, ('spaghetti', 'tomatoes'): 157, ('french fries', 'milk'): 178, ('chocolate', 'eggs'): 249, ('mineral water', 'pancakes'): 253, ('pancakes', 'spaghetti'): 189, ('milk', 'spaghetti'): 266, ('ground beef', 'milk'): 165, ('ground beef', 'mineral water'): 307, ('ground beef', 'spaghetti'): 294, ('chocolate', 'french fries'): 258, ('chocolate', 'mineral water'): 395, ('eggs', 'french fries'): 273, ('french fries', 'mineral water'): 253, ('frozen vegetables', 'mineral water'): 268, ('chocolate', 'frozen vegetables'): 172, ('cake', 'mineral water'): 206, ('french fries', 'green tea'): 214, ('french fries', 'pancakes'): 151, ('chocolate', 'green tea'): 176, ('chocolate', 'spaghetti'): 294, ('chocolate', 'ground beef'): 173, ('chocolate', 'milk'): 241, ('frozen vegetables', 'milk'): 177, ('mineral water', 'soup'): 173, ('olive oil', 'spaghetti'): 172, ('burgers', 'french fries'): 165, ('burgers', 'spaghetti'): 161, ('french fries', 'spaghetti'): 207, ('shrimp', 'spaghetti'): 159, ('eggs', 'green tea'): 191, ('eggs', 'milk'): 231, ('eggs', 'pancakes'): 163, ('eggs', 'frozen vegetables'): 163}}
#关联规则： [{olive oil} -> {mineral water}, {ground beef} -> {mineral water}, {soup} -> {mineral water}]
"
