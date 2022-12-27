if __name__ == '__main__':
    N = int(input())
    answer = []
    for i in range(N):
        task = list(map(str, input().split(" ")))
        operation = task[0]
        if len(task) == 1:
            if operation == "print":
                print(answer)
            elif operation == "sort":
                answer.sort()
            elif operation == "reverse":
                answer.reverse()
            elif operation == "pop":
                answer.pop()
        elif len(task) == 2:
            value = int(task[1])
            if operation == "remove":
                answer.remove(value)
            elif operation == "append":
                answer.append(value)
        elif len(task) == 3:
            index = int(task[1])
            value = int(task[2])
            if operation == "insert":
                answer.insert(index, value)
        
