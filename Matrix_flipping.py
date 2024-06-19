def transpose_matrix(matrix, rows, cols):
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    index = 0
    while index < len(input_data):
        if input_data[index].strip() == '':
            index += 1
            continue
        rows, cols = map(int, input_data[index].strip().split())
        index += 1
        matrix = []
        for _ in range(rows):
            matrix.append(list(map(int, input_data[index].strip().split())))
            index += 1
        transposed_matrix = transpose_matrix(matrix, rows, cols)
        for row in transposed_matrix:
            print(' '.join(map(str, row)))
        print()

if __name__ == "__main__":
    main()
