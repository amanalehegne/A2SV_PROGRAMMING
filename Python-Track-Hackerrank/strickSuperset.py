# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(list(map(int, input().split(" "))))
setsize = int(input())
check = True
for i in range(setsize):
    subset = set(list(map(int, input().split(" "))))
    if (not superset.difference(subset)) or (subset.difference(superset)):
        print(False)
        check = False
        break

if check:
    print(True)
