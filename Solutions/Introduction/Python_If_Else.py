#!/bin/python3

import math
import os
import random
import re
import sys
def even(n):
    if n%2 ==0:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input().strip())
    if even(n) == False:
        print('Weird')
    else:
        if 2<=n<=5:
            print("Not Weird")
        elif n<=20:
            print("Weird")
        else:
            print('Not Weird')
