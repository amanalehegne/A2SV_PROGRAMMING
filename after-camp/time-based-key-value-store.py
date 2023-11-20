class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.dic.get(key)
        if not values:
            return ""
        
        left = 0
        right = len(values) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if values[midPoint][0] > timestamp:
                right = midPoint - 1
            else:
                left = midPoint + 1
        if right < 0:
            return ""
        else:
            return values[right][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)