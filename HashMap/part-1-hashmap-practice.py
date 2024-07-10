# Hash Map Using the List 
# stock_prices= []
# with open('stock_prices.csv','r') as f:
#     for line in f: 
#         day , price = line.split(',')
#         price = float(price)
#         stock_prices.append([day, price])


# print(stock_prices)
# Hash Map using the dictionary
# data structure version of dictionary
 
# stock_price_dt = {}

# with open('stock_prices.csv','r') as f:
#     for lins in f:
#         day , price = lins.split(',')
#         price = float(price)
#         stock_price_dt[day] = price

# print(stock_price_dt)


# print(ord('a'))

from typing import Any


class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None]*self.MAX

    def get_hash(self, key):
        sum = 0 
        for c in key:
            sum += ord(c)
        return sum % self.MAX
    
    def __setitem__(self,key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
         h = self.get_hash(key)
         self.arr[h] = None



h = HashTable()
h['march 6'] = 302
h['march 11'] = 78
del h['march 11'] 
print(h['march 11'])
# hs_map['march 11'] = 78


