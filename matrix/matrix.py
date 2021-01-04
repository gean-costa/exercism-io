class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, m.split(' ')))
                       for m in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]
