length1 = int(input())
arr1 = set(input().split(" "))
length2 = int(input())
arr2 = set(input().split(" "))

answer = arr1.difference(arr2)
print(len(answer))
