#Program to display data type, memory address, size in bytes
import sys

x = input("Enter any value: ")

print("Data Type:", type(x))
print("Memory Address:", id(x))
print("Size in bytes:", sys.getsizeof(x))
