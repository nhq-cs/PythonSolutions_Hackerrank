#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = s.split(" ")
    result =''
    for item in name:
        result += item.capitalize() + " "
    return result.strip()
if __name__ == '__main__':