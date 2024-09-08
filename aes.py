N_ROWS = 4
N_COLS = 4


def CyclicShift(row, shift):
  return row[shift:] + row[:shift]


def ShiftRows(state):
  for row_index in range(N_ROWS):
    state[row_index] = CyclicShift(state[row_index], row_index)
  return state


def BuildExpressionString(column, matrix_row):
  expression = "("
  for (i, coefficient) in enumerate(matrix_row):
    term = str(coefficient) + "*" + column[i]
    should_insert_plus = i < len(matrix_row) - 1
    expression += term

    if should_insert_plus:
      expression += " + "
  return expression + ")"


def GetStateColumn(state, column_index):
  column = []
  for row in state:
    column.append(row[column_index])
  return column


def MultiplyColumn(column):
  matrix = [
      [2, 3, 1, 1],
      [1, 2, 3, 1],
      [1, 1, 2, 3],
      [3, 1, 1, 2]
  ]

  new_column = []
  for row in matrix:
    new_element = BuildExpressionString(column, row)
    new_column.append(new_element)
  return new_column


def MixColumns(state):
  new_columns = []
  for column_index in range(N_COLS):
    column = GetStateColumn(state, column_index)
    new_column = MultiplyColumn(column)
    new_columns.append(new_column)

  return Transpose(new_columns)


def Transpose(matrix):
  return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def PrettyPrint(matrix):
  for row in matrix:
    print(row)


def PrettyPrint2(matrix):
  for row in matrix:
    for element in row:
      print(element)


state = [["x0", "x4", "x8", "x12"],
         ["x1", "x5", "x9", "x13"],
         ["x2", "x6", "x10", "x14"],
         ["x3", "x7", "x11", "x15"]]


def AESRound(state):
  return MixColumns(ShiftRows(state))


def AES(state, rounds):
  for r in range(rounds):
    state = AESRound(state)
  return state


PrettyPrint2(AES(state, 1))
print('\n')
PrettyPrint(AES(state, 2))
ans = '''
[['x0', 'x4', 'x8', 'x12'], ['x5', 'x9', 'x13', 'x1'], ['x10', 'x14', 'x2', 'x6'], ['x15', 'x3', 'x7', 'x11']]

[['2*x0 + 3*x5 + 1*x10 + 1*x15', '2*x4 + 3*x9 + 1*x14 + 1*x3', '2*x8 + 3*x13 + 1*x2 + 1*x7', '2*x12 + 3*x1 + 1*x6 + 1*x11'], ['1*x0 + 2*x5 + 3*x10 + 1*x15', '1*x4 + 2*x9 + 3*x14 + 1*x3', '1*x8 + 2*x13 + 3*x2 + 1*x7', '1*x12 + 2*x1 + 3*x6 + 1*x11'], ['1*x0 + 1*x5 + 2*x10 + 3*x15', '1*x4 + 1*x9 + 2*x14 + 3*x3', '1*x8 + 1*x13 + 2*x2 + 3*x7', '1*x12 + 1*x1 + 2*x6 + 3*x11'], ['3*x0 + 1*x5 + 1*x10 + 2*x15', '3*x4 + 1*x9 + 1*x14 + 2*x3', '3*x8 + 1*x13 + 1*x2 + 2*x7', '3*x12 + 1*x1 + 1*x6 + 2*x11']]

x0,x5,x10,x15

x2,x7,x8,x13

no

12

x0:1,x5:1,x10:1,x15:1

x0:0,x1:0,x2:0,x3:0,x4:0,x5:0,x6:0,x7:0,x8:0,x9:0,x10:0,x11:0,x12:0,x13:0,x14:0,x15:0

x0

(2*(2*x0 + 3*x1 + 1*x2 + 1*x3) + 3*(1*x0 + 2*x1 + 3*x2 + 1*x3) + 1*(1*x0 + 1*x1 + 2*x2 + 3*x3) + 1*(3*x0 + 1*x1 + 1*x2 + 2*x3))

no

'''
