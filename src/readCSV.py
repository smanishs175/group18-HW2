import csv
import re
from pathlib import Path

def coerce(s):

    def fun(s1):
        if s1 in ["True", "true"]:
            return True
        
        elif s1 in ["False", "false"]:
            return False
            
        return s1

    # coerce s based on it's type
    try:
        temp = float(s)
        return temp
    except ValueError as e:
        # can't cast to a number or int so we remove trailing and leading whitespaces
        s = s.strip()
        return fun(s)

def Csv(fname=None, fun=None, sep=",", src=None, s=None,t=None):
    
    # build absolute path from relative path input test file
    path = Path(__file__).parent / src
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=sep)
        for row in reader:
            t = {}
            for s1 in row:
                t[1 + len(t)] = coerce(s1)
            fun(t)
            
                
            
            
    

