def number_generator(n):
    for i in range(n):
        yield i


gen = number_generator(11)

for i in range(7): 
  print(next(gen))
 
# for i in gen:
#     print(i)


