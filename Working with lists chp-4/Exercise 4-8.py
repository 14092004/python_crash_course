# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes , and use a for loop to print outthe value of each cube.
squares = []
for value in range(1,11):
    square = value**3
    squares.append(square)
print(squares)
