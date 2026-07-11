def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = []

    for row in matrix:
        result.append(row[::-1])

    return result