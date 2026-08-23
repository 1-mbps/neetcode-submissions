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
                # print(f"LOCATION: {rown, coln} - NUM: {n}")
                if rows[rown][index]:
                    # print(f"ROW FALSE:\n- row: {row}\n- tracker: {rows[rown]} (row {rown})\n- LOCATION:{rown,coln}\n")
                    for rrow in rows:
                        print(rrow)
                    return False
                if cols[coln][index]:
                    # print("COL FALSE")
                    return False
                coords = (int(rown/3),int(coln/3))
                if subboxes[coords][index]:
                    # print("SUBBOX FALSE")
                    return False
                # print(f"LOCATION: {rown, coln}. Making true ROWN = {rown}, INDEX = {index}.")
                rows[rown][index] = True
                cols[coln][index] = True
                subboxes[(int(rown/3),int(coln/3))][index] = True
        
        return True

        