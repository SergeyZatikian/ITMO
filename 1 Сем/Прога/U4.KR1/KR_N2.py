from random import randint
product = ["банан", "яблоко", "вишня"]
cost = []
price = []
pr = list()
for i in range(len(product)):
    cost.append(randint(20,60))
print(cost)
for i in range(len(cost)):
    price.append(round(cost[i]*1.15))
print(price)
pr = zip(product, cost, price)
print(list(pr))