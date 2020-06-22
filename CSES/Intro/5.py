n = int(input())
nums = range(1, n+1)
sol = [0] * n
counter = 0
for i in range(2, n+1, 2):
    sol[counter] = i
    counter += 1
for i in range(1, n+1, 2):
    sol[counter] = i
    counter += 1
if 0 in sol or 1 < n <= 3: 
    print("NO SOLUTION")
else:
    ans = ""
    for num in sol:
        ans += str(num) + " "
    print(ans)
