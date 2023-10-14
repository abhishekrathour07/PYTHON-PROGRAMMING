import os 

# os.rename("Library","lib")
os.chdir("lib")
for i in range(30):
    os.rename(f"books {i+1}",f"Book {i+1}")
print(os.getcwd())
