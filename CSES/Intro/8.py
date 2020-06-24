listNums = [int(i) for i in range(1, int(input()) + 1)]
def recursive(curr, arr, idx, goal):
    if goal == 0:
        return curr
    if idx >= len(arr) or goal < 0: return
    include = recursive(curr + " " + str(arr[idx]), arr, idx + 1, goal - arr[idx])
    exclude = recursive(curr, arr, idx + 1, goal)
    if include != None: return include
    else: return exclude

if sum(listNums) % 2 != 0: print("NO")
else:
    print("YES")
    res = [int(i) for i in list(recursive("", listNums, 0, int(sum(listNums) / 2)).split(' ')[1:])]
    print(len(res))
    ans1 = ""
    for ans in res:
        ans1 += str(ans) + " "
    print(ans1)
    ans2 = ""
    count = 0
    for nums in range(1, len(listNums)):
        if nums not in res:
            count += 1
            ans2 += str(nums) + " "
    print(count)
    print(ans2)