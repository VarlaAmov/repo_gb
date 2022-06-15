class Matrix():

    def __init__(self, lst):
        if self.is_data(lst):
            self.data = lst
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    def is_data(self, data):
        set_lenghts = {len(lst) for lst in data}
        if len(set_lenghts) == 1:
            return True
        else:
            return False

    @property
    def dim(self):
        return len(self.data), len(self.data[0])

    def __str__(self):
        rez = ""
        for row in self.data:
            rez += "| "
            for i in row:
                rez += f"{i:3d} "
            rez += "|\n"
        return rez

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Incorrect dimensions for add method")
        lst_final = []
        for i, row1 in enumerate(self.data):
            row2 = []
            for j, el in enumerate(row1):
                row2.append(self.data[i][j] + other.data[i][j] )
            lst_final.append(row2)
        return Matrix(lst_final)

m1 = Matrix([[11,2,3],[4,5,6],[11,8,9]])
m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
m3 = Matrix([[1,1],[1,1],[1,1]])
m4 = m1 + m2
print(m1)
print(m4)
