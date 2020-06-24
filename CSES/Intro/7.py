grid = int(input())
def solve(n):
    return n * n * (n * n - 1) / 2 - 4 * (n - 1) * (n - 2)
for i in range(1, grid + 1):
    print(int(solve(i)))