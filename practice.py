# import threading

# def print_numbers():
#     for i in range(5):
#         print(i)

# def print_letters():
#     for letter in 'abcde':
#         print(letter)

# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Both threads finished execution.")
first =0
last =9
middle = int(first+last)/2
print(int(middle))