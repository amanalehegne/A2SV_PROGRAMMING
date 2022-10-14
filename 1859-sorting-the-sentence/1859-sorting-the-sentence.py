class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        for i in s:
            if i.isdigit():
                arr.append(0)
        word = ""
        for i in s:
            if i.isdigit():
                word.strip()
                arr[int(i) - 1] = word
                word = ""
            elif i == " ":
                continue
            else:
                word += i
        return " ".join(arr)