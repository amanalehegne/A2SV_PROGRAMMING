def no_idea(first, second, third):
    score = 0
    a, b = dict(), dict()
    for i in second:
        a[i] = True
    for i in third:
        b[i] = False

    for i in first:
        if i in a:
            score += 1
        elif i in b:
            score -= 1
    return score


size = input().split(" ")
first = input().split(" ")
second = input().split(" ")
third = input().split(" ")
print(no_idea(first, second, third))
