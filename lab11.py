with open("word.txt","r") as file:
	data = file.read()
	letter_count = {}
	for ch in data:
		if ch not in letter_count.keys():
			letter_count[ch]=1
		else:
			letter_count[ch]+=1
print(data)
for i in letter_count:
	print(i,":",letter_count[i])
print(letter_count)
