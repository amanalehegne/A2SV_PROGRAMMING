class Solution:
    def calculate(self, s: str) -> int:
        dic = {"+": 1, "-": 1, "*": 3, "/": 3}
        num, op = [], []
        s = s.strip()
        number = ""
        for i in s:
            if i == " ":
                continue
            if i.isdigit():
                number += i
            else:
                num.append(int(number))
                number = ""
                while op and dic.get(op[-1]) >= dic.get(i):
                    num2 = num.pop()
                    num1 = num.pop()
                    value = self.evaluate(num1, num2, op.pop())
                    num.append(value)
                op.append(i)
        num.append(int(number))
        while op:
            num2 = num.pop()
            num1 = num.pop()
            value = self.evaluate(num1, num2, op.pop())
            num.append(value)
        return num[0]


    def evaluate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 // num2