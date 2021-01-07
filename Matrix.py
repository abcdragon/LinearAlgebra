class Matrix:
    def __init__(self, array):
        if isinstance(array[0], int):
            array = [array]

        self.__shape = (len(array), len(array[0]))
        self.__matrix = array

    def __getitem__(self, item):
        if isinstance(item, tuple):
            if isinstance(item[0], slice):
                if isinstance(item[1], int):
                    return Matrix([[r[item[1]]] for r in self.__matrix[item[0]]])

                if isinstance(item[1], slice):
                    return Matrix([[c for c in r[item[1]]] for r in self.__matrix[item[0]]])

            if isinstance(item[0], int):
                if isinstance(item[1], slice):
                    return Matrix(self.__matrix[item[0]][item[1]])

                if isinstance(item[1], int):
                    return self.__matrix[item[0]][item[1]]

        if isinstance(item, int):
            return Matrix(self.__matrix[item])

        raise Exception('올바르지 않은 접근입니다.')
