def findPatter(arr):
    size = len(arr[0])
    answer = ["?"] * size
    for pattern in arr:
        for i, char in enumerate(pattern):
            if answer[i] == "?":
                answer[i] = char
            elif char == "?":
                continue
            else:
                if answer[i] != char:
                    answer[i] = "remove"
    for i in range(len(answer)):
        if answer[i] == "?":
            answer[i] = "c"
        elif answer[i] == "remove":
            answer[i] = "?"
    return "".join(answer)
 
 
size = int(input())
arr = []
for i in range(size):
    arr.append(input())
 
print(findPatter(arr))
