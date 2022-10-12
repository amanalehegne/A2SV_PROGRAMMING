class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        stack = []
        dir = dot = ""
        for i in path:
            if i == '/':
                if dir:
                    stack.append(dir)
                elif len(dot) > 1:
                    if len(dot) == 2:
                        if stack:
                            stack.pop()
                    else:
                        stack.append(dot)
                dir = dot = ""
            elif i == '.' and not dir:
                dot += i
            else:
                dir += dot
                dot = ""
                dir += i
        return "/" + "/".join(stack)