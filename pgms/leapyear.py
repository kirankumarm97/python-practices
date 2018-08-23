#!/bin/python3

import sys

def solve(year):
    if year%4==0:
        if (year//4)%2==0:
            return 256-244
    
        print("hello")
        return 256-243  

year = int(input().strip())
result = solve(year)
result=str(result)+'.09.'+str(year)
print(result)
