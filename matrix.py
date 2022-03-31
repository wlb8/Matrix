
import copy


def Reflexive(matrix):
    '''Loop through once checking if for every snake eyes value that it is greater than 0'''
    count = 0
    for i in range(len(matrix)):
        if (matrix[i][i] > 0):
            count += 1
    if count == len(matrix):
        return True
    else:
        return False


def Symmetry(matrix):
    '''Find out using 4 nested loops if the matrix is symmetric'''
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for h in range(len(matrix)):
                for g in range(len(matrix)):
                    if matrix[i][j] == matrix[h][g]:
                        count += 1
    if count == (len(matrix)*len(matrix)):
        return True
    else:
        return False
                    



def Transitive(matrix, matrixSquared):
    '''Compare each values in the matrix and squared matrix. As long as they're both not = 0 then it is transitive'''
    squaredCount = 0
    regCount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 0:
                regCount += 1
            if matrixSquared[i][j] > 0:
                squaredCount += 0
    if regCount == squaredCount:
        return True
    else:
        return False

if __name__ == "__main__":
    matrix=[]
    matrixSquared=[]
    print("Enter the size of the matrix")
    cols = int(input())
    for i in range(1, cols+1):
        print("Enter row", i, " ")
        temp_rows = [int(i) for i in input().split()]
        new_list = copy.copy(temp_rows)
        matrix.append(new_list)
        temp_rows.clear()
    
    #print matrix out
    print(end='\n')
    print("MATRIX:")
    print(end='\n')
    for i in range(len(matrix)):
        print(matrix[i], end="\n")
    
    #Squaring the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrixValue=0
            for h in range(len(matrix)):
                temp = matrix[i][h] * matrix[h][j]
                matrixValue+=temp
            temp_rows.append(matrixValue)
        new_list = copy.copy(temp_rows)
        matrixSquared.append(new_list)
        temp_rows.clear()
    print(end='\n')
    print("SQAURED MATRIX:", end='\n')
    for i in range(len(matrixSquared)):
        print(matrixSquared[i], end="\n")
    
    isReflexive = Reflexive(matrix)
    
    print(Reflexive(matrix))
    print(Symmetry(matrix))
    print(Transitive(matrix, matrixSquared))

        

