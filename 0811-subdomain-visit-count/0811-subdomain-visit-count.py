class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for domain in cpdomains:
            visit, link = domain.split(" ")
            linkList = link.split(".")
            length = len(linkList)
            string = ""
            for i in range(length):
                if string:
                    string = linkList[length - 1 - i] + "." + string
                else:
                    string = linkList[length - 1 - i]
                dic[string] += int(visit)

        answer = []
        for key in dic:
            string = str(dic.get(key)) + " " + key
            answer.append(string)

        return answer
        