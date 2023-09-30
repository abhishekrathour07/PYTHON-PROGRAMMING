
import sys
str = 'abhishek'
i = 4
j =10.45
print(len(str))
print(bool(i))
print(type(str)) #size of string = 49 byte
print(type(i))
print(sys.getsizeof(i))  # size of int = 28 byte
print(sys.getsizeof(j)) #size of float = 24 byte
