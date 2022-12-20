def swap_case(s):
    temp = s.split(" ")
    ans = []
    for word in temp:
        ans_temp = []
        for i in word:
            if i.isupper(): ans_temp.append(i.lower())
            else: ans_temp.append(i.upper())
        ans.append("".join(ans_temp))
    return " ".join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
