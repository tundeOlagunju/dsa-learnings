# https://leetcode.com/problems/word-squares/editorial/ - Another problem backtacking with mp is uses

# This problem is Word Search II on leetcode
NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def neighbours(board, pos):
    for n in NEIGHBOURS:
        new_pos = (pos[0] + n[0], pos[1] + n[1])
        if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]):
            yield new_pos

def walk_board(board, pos, partials, output, visited, path):
    visited |= frozenset((pos,))
    path += board[pos[0]][pos[1]]
    if path not in partials:
        return
    if partials[path]:
        output.add(path)
    for new_pos in neighbours(board, pos):
        if new_pos not in visited:
            walk_board(board, new_pos, partials, output, visited, path)

def find_words(board, partials, output):
    for start_row in range(0, len(board)):
        for start_col in range(0, len(board[0])):
            visited = frozenset()
            path = ""
            walk_board(board, (start_row, start_col), partials, output, visited, path)

def get_partials(words):
    partials = {}
    for word in words:
        partials[word] = True
        for i in range(1, len(word)):
            p = word[:i]
            if p not in partials:
                partials[p] = False
    return partials

def boggle_board(board, words):
    partials = get_partials(words)
    print(partials)
    output = set()
    find_words(board, partials, output)
    return output

def main():
    board = [
     ["t", "h", "i", "s", "i", "s", "a"],
     ["s", "i", "m", "p", "l", "e", "x"],
     ["b", "x", "x", "x", "x", "e", "b"],
     ["x", "o", "g", "g", "l", "x", "o"],
     ["x", "x", "x", "D", "T", "r", "a"],
     ["R", "E", "P", "E", "A", "d", "x"],
     ["x", "x", "x", "x", "x", "x", "x"],
     ["N", "O", "T", "R", "E", "-", "P"],
     ["x", "x", "D", "E", "T", "A", "E"],
    ]
    words = [
     "this", "is", "not", "a", "simple", "boggle",
     "board", "test", "REPEATED", "NOTRE-PEATED"
    ]
    output = boggle_board(board, words)
    print(output)

if __name__ == "__main__":
    main()
