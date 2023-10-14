with open("File2.txt","r") as f:
    f.seek(10)
    print(f.tell)
    data = f.read()
    print(data)
