import os 
import sys
print(os.getcwd())
os.chdir("lib")
# path = "D:\MyCodes\PYTHON PROGRAMMING/lib" --> We can use this also
# os.chdir(path)

for i in range(30):
    os.rmdir(f"books {i+1}")
