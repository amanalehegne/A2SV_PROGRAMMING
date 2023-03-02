def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for start, end, val in queries:
        arr[start - 1] += val
        arr[end] -= val
    res = arr[0]
    for i in range(1, n):
        arr[i] += arr[i - 1]
        res = max(res, arr[i])
    
    return res
