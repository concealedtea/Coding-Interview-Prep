numTests = int(input())
tests = [[]] * numTests
for i in range(numTests):
    tests[i] = [int(i) for i in list(input().split(' '))]
def solve(row, col):
    base = 1
    if row > col:
        if row % 2 == 0:
            base = row ** 2 - col + 1
        else:
            base = (row - 1) ** 2 + col
    else:
        if col % 2 == 1:
            base = col ** 2 - row + 1
        else:
            base = (col - 1) ** 2 + row
    return base

for test in tests:
    print(solve(test[0], test[1]))
