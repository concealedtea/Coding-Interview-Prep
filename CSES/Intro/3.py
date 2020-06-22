chars = str(input())
start = end = 0
maxLen = 0
while end < len(chars):
    if chars[start] == chars[end]:
        if end - start > maxLen: maxLen = end-start
        end += 1
    else:
        start = end
        end += 1
print(maxLen + 1)