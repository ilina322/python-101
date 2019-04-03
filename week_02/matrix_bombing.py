import copy

def matrix_bombing_plan(matrix):
    damage_list = {}
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            new_matrix = bomb_neighbours(row, col, matrix)
            matrix_sum = find_matrix_sum(new_matrix)
            damage_list[(row,col)] = matrix_sum
    return damage_list

def find_matrix_sum(matrix):
    element_sum = 0
    for row in matrix:
        for element_value in row:
            element_sum += element_value
    return element_sum


def bomb_neighbours(row, col, matrix):
    new_matrix = copy.deepcopy(matrix)
    neighbours = find_neighbours(row, col, matrix)
    element_value = matrix[row][col]
    for neighbour in neighbours:
        curr_row, curr_col = neighbour
        new_matrix[curr_row][curr_col] -= element_value
        if new_matrix[curr_row][curr_col] < 0:
            new_matrix[curr_row][curr_col] = 0

    return new_matrix

def find_neighbours(row, col, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    neighbours = [(a,b) for a in range(row - 1, row + 2) if a >= 0 and a < rows for b in range(col - 1, col + 2) if b >= 0 and b < cols]
    neighbours.remove((row,col))
    return neighbours

def main():
    matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(matr))

if __name__ == '__main__':
    main()

