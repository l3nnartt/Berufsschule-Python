# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print('Starting Zweidimensionale_Listen.py')


# Aufgabe 1:
# Schreiben Sie eine Funktion namens matrix_transpose(matrix),
# die eine zweidimensionale Liste (eine Matrix) als Parameter entgegennimmt
# und eine neue Matrix zurückgibt, die die transponierte Version
# der ursprünglichen Matrix darstellt.
#
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
#
# # Die transponierte Matrix sieht wie folgt aus:
# # [
# #   [1, 4],
# #   [2, 5],
# #   [3, 6]
# # ]

def transpose_matrix(matrix):
  new_matrix = []
  matrix_lenght = len(matrix[0])
  for x in range(matrix_lenght):
    new_matrix.append([])
    for y in range(len(matrix)):
      new_matrix[x].append(matrix[y][x])
  return new_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix))
