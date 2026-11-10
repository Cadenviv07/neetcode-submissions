class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                char val = board[r][c];
                if(val == '.') continue;

                int squareIndex = (r/3) * 3 + (c/3);
                rows.putIfAbsent(r, new HashSet<>());
                cols.putIfAbsent(c, new HashSet<>());
                squares.putIfAbsent(squareIndex, new HashSet<>());

              
                if (!rows.get(r).add(val) ||
                    !cols.get(c).add(val) ||
                    !squares.get(squareIndex).add(val)) {
                    return false;
                }

            }
        }

        return true;
    }
}
