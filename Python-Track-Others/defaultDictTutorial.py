# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size1, size2 = list(map(int, input().split()))
dic = defaultdict(list)
for i in range(size1):
    dic[input()].append(i + 1)

for i in range(size2):
    temp = input()
    if dic.get(temp):
        print(*dic.get(temp))
    else:
        print(-1)
