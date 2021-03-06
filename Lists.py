import random

# Randomly generated lists
listOfBooks = []
for i in range(10):
    listOfBooks.append(random.randrange(1, 10))

listOfNumbers = list(range(0, 101, 10))

print(listOfNumbers)
print(type(listOfBooks))

# Operations on Lists:

# -1 index is the last element. Then it counts down form the end for numbers before -1:
print(listOfBooks[0])
# Slice (first element : last element)
print("Slice from 2nd element to the 4th element:")
print(listOfBooks[2:5])

# Maximum and Minimum of a list
print(max(listOfBooks))
print(min(listOfBooks))

# Add to a list
listOfBooks.append(120)
# print(listOfBooks)

# Reverse a list
listOfBooks.reverse()
print(listOfBooks)