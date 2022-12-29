# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkSuperset(superset, subsetSize):
    for i in range(subsetSize):
        subset = set(list(map(int, input().split(" "))))
        if (not superset.difference(subset)) or (subset.difference(superset)):
            return False

    return True

    
superset = set(list(map(int, input().split(" "))))
subsetSize = int(input())
print(checkSuperset(superset, subsetSize))
