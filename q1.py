# Q1: Initialize an array with 5 numbers, add a new number, and print the updated array

from array import array

numbers = array('i', [1, 2, 3, 4, 5])

numbers.append(6)

print("Updated array:", numbers.tolist())
