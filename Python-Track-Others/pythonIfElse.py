#!/bin/python3

def checkWeird(num):
    if num % 2:
        return "Weird"
    else:
        if (num > 20) or (num in range(2, 6)):
            return "Not Weird"
        else:
            return "Weird"

        

if __name__ == '__main__':
    n = int(input().strip())
    print(checkWeird(n))
