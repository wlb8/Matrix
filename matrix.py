import copy

if __name__ == "__main__":
    matrix=[]
    print("Enter the size of the matrix")
    cols = int(input())
    for i in range(1, cols+1):
        print("Enter row", i, " ")
        temp_rows = [int(i) for i in input().split()]
        new_list = copy.copy(temp_rows)
        matrix.append(new_list)
        temp_rows.clear()
    
    print(end='\n')
    print("MATRIX:")
    print(end='\n')
    for i in range(len(matrix)):
        print(matrix[i], end="\n")
    
