class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def contain(str):
            colon = str.find(':')
            dot = str.find('.')
            if colon != -1 and dot != -1:
                return -1
            elif colon != -1:
                return 0
            elif dot != -1:
                return 1
            else:
                return 2


        def checkIPv4(str):
            arr = str.split('.')
            if len(arr) != 4:
                return "Neither"
            for val in arr:
                if not val.isdigit():
                    return "Neither"
                if (int(val) < 0 or int(val) > 255) or (len(val) > 1 and val[0] == '0'):
                    return "Neither"
            return "IPv4"


        def checkIPv6(str):
            arr = str.split(':')
            if len(arr) != 8:
                return "Neither"
            for val in arr:

                if len(val) > 4 or len(val) == 0:
                    return "Neither"
                for char in val:
                    if char.isdigit() or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F'):
                        continue
                    else:
                        return "Neither"
            return "IPv6"

        val = contain(queryIP)
        res = "Neither"
        if val == 0:
            res = checkIPv6(queryIP)
        elif val == 1:
            res = checkIPv4(queryIP)
        
        return res
        