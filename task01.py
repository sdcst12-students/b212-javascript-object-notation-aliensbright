#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

filename1a = 'task01a.txt'
file1a = open(filename1a,'r')
data1a = file1a.read()
Numbers1a = json.loads(data1a)

filename1b = 'task01b.txt'
file1b = open(filename1b,'r')
data1b = file1b.read()
Numbers1b = json.loads(data1b)

filename1c = 'task01c.txt'
file1c = open(filename1c,'r')
data1c = file1c.read()
Numbers1c = json.loads(data1c)

a=max(Numbers1a)
b=max(Numbers1b)
c=max(Numbers1c)

print(f"task01a: {a}\ntask01b: {b}\ntask01c: {c}")