puzzle = [['R', 'U', 'N', 'A', 'R', 'O', 'U', 'N', 'D', 'D', 'L'],
          ['E', 'D', 'C', 'I', 'T', 'O', 'A', 'H', 'C', 'Y', 'V'],
          ['Z', 'Y', 'U', 'W', 'S', 'W', 'E', 'D', 'Z', 'Y', 'A'],
          ['A', 'K', 'O', 'T', 'C', 'O', 'N', 'V', 'O', 'Y', 'V'],
          ['L', 'S', 'B', 'O', 'S', 'E', 'V', 'R', 'U', 'C', 'I'],
          ['B', 'O', 'B', 'L', 'L', 'C', 'G', 'L', 'P', 'B', 'D'],
          ['L', 'K', 'T', 'E', 'E', 'N', 'A', 'G', 'E', 'D', 'L'],
          ['I', 'S', 'T', 'R', 'E', 'W', 'Z', 'L', 'C', 'G', 'Y'],
          ['A', 'U', 'R', 'A', 'P', 'L', 'E', 'B', 'A', 'Y', 'G'],
          ['R', 'D', 'A', 'T', 'Y', 'T', 'B', 'I', 'W', 'R', 'A'],
          ['T', 'E', 'Y', 'E', 'M', 'R', 'O', 'F', 'I', 'N', 'U']]


def wordsearch(search_string):
    search_string = search_string.upper()

    result = []

    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            if len(search_string) and puzzle[row][column] == search_string:
                result.append((row, column))
            else:
                directions = ((0, -1), (1, -1), (1, 0), (1, 1),
                              (0, 1), (-1, 1), (-1, 0), (-1, -1))

                for direction in directions:
                    currentRow = row
                    currentColumn = column

                    characterPositions = []

                    for i in range(len(search_string)):
                        if currentRow >= len(puzzle) or currentRow < 0 or currentColumn >= len(puzzle) or currentColumn < 0:
                            break

                        if (search_string[i] != puzzle[currentRow][currentColumn]):
                            break

                        characterPositions.append((currentRow, currentColumn))

                        if (i == len(search_string) - 1):
                            result.append(characterPositions)
                            break

                        currentRow += direction[0]
                        currentColumn += direction[1]

    if len(result) == 0:
        return 'Not found!'

    if len(result) == 1:
        return result[0]

    return result
