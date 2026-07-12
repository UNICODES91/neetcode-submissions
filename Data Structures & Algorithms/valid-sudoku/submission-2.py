from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Check rows for validity:
            - loop over rows, add each new entry as key to dict and increase count
            - if duplicate found, count becomes 2 => invalid
        2. Check cols for validity: same as for rows
        3. Check 3x3 grids:
            - divide into 3x3 non-overlapping regions
             r_indices = n_rows // 3
             c_indices = n_cols // 3
             take each block, flatten and repeat as for rows/ cols check

        """

        # row check
        for row in range(9):
            row_dict = defaultdict(int)  # new one for each row
            for col in range(9):
                if board[row][col] == '.':
                    continue
                else:
                    row_dict[board[row][col]] += 1
                    if row_dict[board[row][col]] > 1:
                        return False

        # col check
        for col in range(9):
            col_dict = defaultdict(int)
            for row in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                else:
                    col_dict[val] += 1
                    if col_dict[val] > 1:
                        return False

        # block check
        block_dict = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                bid_col = col // 3
                bid_row = row // 3
                bid = bid_col + bid_row * 3
                # print(f"(row, col)={(row, col)}, (bid_row, bid_col)={(bid_row, bid_col)}, g_bid={bid}")
                if val == '.':
                    continue
                else:
                    if bid not in block_dict:
                        block_dict[bid] = [val]
                    else:
                        if val in block_dict[bid]:
                            return False
                        else:
                            block_dict[bid].append(val)

        return True