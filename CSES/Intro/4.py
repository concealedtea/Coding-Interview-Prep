size = int(input())
contents = [int(i) for i in list(input().split(' '))]
numChanges = 0
for i in range(1, size):
    while contents[i] < contents[i-1]:
        numChanges += contents[i-1] - contents[i]
        contents[i] = contents[i-1]
print(str(numChanges))
