n = int(input())
listOfN = [int(i) for i in list(input().split(' '))]
expected = sum(range(n+1))
print(expected - sum(listOfN))