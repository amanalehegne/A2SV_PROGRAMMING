class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            lst = path.split(" ")
            directory = lst[0]
            filesLength = len(lst)
            for i in range(1, filesLength):
                file = lst[i]
                fileLst = file.split("(")
                fileName = fileLst[0]
                fileContent = fileLst[-1][:-1]
                dic[fileContent].append((directory + "/" + fileName))

        answer = []
        for key in dic:
            if len(dic.get(key)) > 1:
                answer.append(dic.get(key))

        return answer
        