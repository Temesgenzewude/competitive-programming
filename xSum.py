
def compute_sum(i, j, n, m, board):
    # Computes the sum of all cells attacked by the bishop from cell (i,j)
    s = board[i][j]
    r, c = i, j
    while r > 0 and c < m - 1:
        r -= 1
        c += 1
        s += board[r][c]
    r, c = i, j
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        s += board[r][c]
    r, c = i, j
    while r < n - 1 and c < m - 1:
        r += 1
        c += 1
        s += board[r][c]
    r, c = i, j
    while r < n - 1 and c > 0:
        r += 1
        c -= 1
        s += board[r][c]
    return s


def xSum():
    
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        max_sum = 0
        for i in range(n):
            for j in range(m):
                s = compute_sum(i, j, n, m, board)
                max_sum = max(max_sum, s)
        print(max_sum)
        
        
xSum()
