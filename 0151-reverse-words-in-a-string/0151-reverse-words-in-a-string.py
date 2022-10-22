class Solution:
    def reverseWords(self, s: str) -> str:
        prev = temp = ""
        arr = []
        for i in s:
            if i != " ":
                temp += i
            elif prev == " " and i == " ":
                continue
            else:
                arr.append(temp)
                temp = ""
            prev = i
        if temp:
            arr.append(temp)

        l, r = 0, len(arr) - 1
        while l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
        return " ".join(arr).strip(" ")