from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func1(a,b):
    time.sleep(3)
    return a*b


print(func1(2,3))
print("Done for 2,3")
print(func1(4,5))
print("Done for 4,5")
print(func1(3,3))
print("Done for 3,3")

print(func1(2,3))
print("Done for 2,3")
print(func1(4,5))
print("Done for 4,5")
print(func1(3,3))
print("Done for 3,3")

