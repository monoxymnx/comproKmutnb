import numpy as np

random_matrix = np.random.randint(1, 10, (3, 3))
print(random_matrix)

matrix_sum = np.sum(random_matrix)
print("Sum of all elements:", matrix_sum)

matrix_mean = np.mean(random_matrix)
print("Mean of all elements:", matrix_mean)

transposed_matrix = np.transpose(random_matrix)
print("Transposed matrix:")
print(transposed_matrix)