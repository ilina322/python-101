import unittest
from matrix_bombing import find_neighbours, bomb_neighbours, matrix_bombing_plan, find_matrix_sum
class TestMatrixBombingPlan(unittest.TestCase):

    def test_when_neighbours_are_outside_matrix_then_dont_include_them(self):
        row = 0 
        col = 2
        matrix = [[1,2,3], [4,5,6], [7,8,9]]
        expected_result = set([(1,1),(0,1), (1,2)])
        self.assertEqual(set(find_neighbours(row, col, matrix)), expected_result)

    def test_when_matrix_is_bombed_then_return_new_matrix(self):
        row = 0 
        col = 0
        matrix = [[1,2,3], [4,5,6], [7,8,9]]
        expected_result = [[1,1,3], [3,4,6], [7,8,9]]
        neighbours = find_neighbours(row,col,matrix)
        self.assertEqual(expected_result, bomb_neighbours(row, col, matrix))

    def test_when_matrix_is_summed_then_return_its_sum(self):
        matrix = [[1,1,1], [1,1,1], [1,1,1]]
        expected_result = 9
        self.assertEqual(find_matrix_sum(matrix), expected_result)



if __name__ == '__main__':
    unittest.main()