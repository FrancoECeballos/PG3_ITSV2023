class Matriz():
    def search_matrix(self,matrix,target):
        for i in range(len(matrix)-1):
            for j in range(0, len(matrix)-i-1):
                if matrix[j] > matrix[j + 1]:
                    matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

        if target in matrix:
            return True
        else:
            return False