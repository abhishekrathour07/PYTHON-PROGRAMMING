with open("lab11.txt", 'r') as file:
    content = file.read()
    # Creating a dictionary to store character frequencies
    char_frequency = {}
    # Counting the frequency of each character
    for char in content:
        if char in char_frequency.keys():
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    # Displaying the results
    print(char_frequency)
    print("Character frequency in the file:")
    for char, frequency in char_frequency.items():
        print(f"{char}: {frequency}")
