def orderWords(arr):
    for lst in arr:
        words = lst.split()
        answer = []
 
        for word in words:
            number = 0
            temp = []
            for char in word:
                if char.isdigit():
                    number = (number * 10) + int(char)
                else:
                    temp.append(char)
            answer.append([number, "".join(temp)])
        answer.sort()
        res = []
        for i, word in answer:
            res.append(word)
        print(*res)
        
 
 
size = int(input())
arr = []
for i in range(size):
    arr.append(input())
 
orderWords(arr)
