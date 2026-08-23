class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        subboxes = {}
        
        for i in range(3):
            for j in range(3):
                subboxes[(i,j)] = [False for _ in range(9)]

        for rown, row in enumerate(board):
            for coln, n in enumerate(row):
                if n == '.':
                    continue
                index = int(n)-1
                if rows[rown][index]:
                    for rrow in rows:
                        print(rrow)
                    return False
                if cols[coln][index]:
                    return False
                coords = (int(rown/3),int(coln/3))
                if subboxes[coords][index]:
                    return False
                rows[rown][index] = True
                cols[coln][index] = True
                subboxes[(int(rown/3),int(coln/3))][index] = True
        
        return True

        