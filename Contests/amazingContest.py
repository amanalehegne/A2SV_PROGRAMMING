def isAmazing(contests, length):
    high = contests[0]
    low = contests[0]
    count = 0
    for i in range(1, length):
        value = contests[i]
        if value > high:
            count += 1
            high = value
        elif value < low:
            count += 1
            low = value
    return count
 
 
size = int(input())
contests = list(map(int, input().split(" ")))
print(isAmazing(contests, size))
