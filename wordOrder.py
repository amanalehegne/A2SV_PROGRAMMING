def word_order(words):
    dic = dict()
    for i in words:
        dic[i] = 1 + dic.get(i, 0)
    ans = list(dic.values())
    print(len(ans))
    print(*ans)


x = int(input())
words = []
for i in range(x):
    words.append(input())

word_order(words)
