# Matrices

# Creating a simple matrix
def create_matrix(rows, columns):
    return [([0] * columns) for _ in range(rows)]

print(create_matrix(5, 3))

