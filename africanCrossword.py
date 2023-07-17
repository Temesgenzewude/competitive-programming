n, m = map(int, input().split())

grid = [input() for _ in range(n)]

row_freqs = [{} for _ in range(n)]
col_freqs = [{} for _ in range(m)]

for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        row_freqs[i][letter] = row_freqs[i].get(letter, 0) + 1
        col_freqs[j][letter] = col_freqs[j].get(letter, 0) + 1

crossed_out = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        if row_freqs[i][letter] == 1 and col_freqs[j][letter] == 1:
            crossed_out[i][j] = False
        else:
            crossed_out[i][j] = True

encrypted_word = ''

for i in range(n):
    for j in range(m):
        if not crossed_out[i][j]:
            encrypted_word += grid[i][j]

print(encrypted_word)
