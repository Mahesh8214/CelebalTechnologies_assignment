rows = 5

# Lower Triangular
print("Lower Triangular :")
for i in range(1, rows + 1):
    print("* " * i)

# Upper Triangular
print("\nUpper Triangular :")
for i in range(rows, 0, -1):
    print("* " * i)

# Pyramid
print("\n Pyramid :")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)