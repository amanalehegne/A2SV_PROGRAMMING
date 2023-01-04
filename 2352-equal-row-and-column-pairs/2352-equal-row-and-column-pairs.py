class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        nums = defaultdict(int)
        for arr in grid:
            temp = "".join(str(i) + "," for i in arr)
            nums[temp] += 1

        length = len(arr)
        count = 0
        for i in range(length):
            temp = []
            for j in range(length):
                temp.append(grid[j][i])
            string = "".join(str(i) + "," for i in temp)
            if nums.get(string):
                count += nums.get(string)
        return count
        