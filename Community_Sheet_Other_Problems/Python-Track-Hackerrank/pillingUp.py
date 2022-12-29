def piling_up(cubes):
    for cube in cubes:
        temp = True
        for i in range(1, len(cube) - 1):
            if int(cube[i]) > int(cube[i - 1]) and int(cube[i]) > int(cube[i + 1]):
                temp = False
                break
        if temp: print("Yes")
        else: print("No")


test_cases = int(input())
temp = []
for i in range(test_cases):
    n = input()
    temp.append(input().split(" "))
piling_up(temp)
