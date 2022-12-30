def checkSize(shirts):
    shirt1, shirt2 = shirts.split(" ")
    index1 = len(shirt1) - 1
    index2 = len(shirt2) - 1

    dic = {"S": 2, "M": 3, "L": 4, "X": 1}

    if shirt1[index1] == shirt2[index2] == "S":
        if len(shirt1) > len(shirt2):
            return "<"
        elif len(shirt1) < len(shirt2):
            return ">"
        return "="

    sum1 = 0
    sum2 = 0

    while index1 >= 0 and index2 >= 0:
        sum1 += dic.get(shirt1[index1])
        sum2 += dic.get(shirt2[index2])
        if sum1 > sum2:
            return ">"
        elif sum1 < sum2:
            return "<"
        index1 -= 1
        index2 -= 1

    if index1 >= 0:
        return ">"
    elif index2 >= 0:
        return "<"
    else:
        return "="




testCase = []
size = int(input())
for i in range(size):
    testCase.append(input())

for i in testCase:
    print(checkSize(i))
