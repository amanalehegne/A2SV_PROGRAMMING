def whatTheKingSays(words):
    for word in words:
        repeat = word[0] + word[1]
        print(repeat+ "...", word + "?")
 
 
size = int(input())
arr = []
for i in range(size):
    arr.append(input())
 
whatTheKingSays(arr)
