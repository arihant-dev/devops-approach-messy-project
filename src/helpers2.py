import random

def getData():
    data = ["apple", "banana", "cherry", "dates", "eggplant"]
    idx = random.randint(0, len(data)-1)
    return data[idx]
