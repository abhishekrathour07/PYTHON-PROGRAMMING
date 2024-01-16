# def even(x):
#     return x % 2 == 0
a = [2, 5, 7, 8, 10, 13, 16]
result = filter(lambda x: x%2==0, a)
print('Original List :', a)
print('Filtered List :', list(result))
