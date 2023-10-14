# # create File .
# file = open("file.txt","x")

# Write onto the File. 
file = open("file.txt","w")
file.write(" Hello this is abhishek singh ")
file.close()

# Append operation . 
file = open("file.txt","a")
file.write(" Hello this is abhishek singh ")
file.close()

# Read file
file = open("file.txt","r")
f = file.read()
print(f)

file.close()
