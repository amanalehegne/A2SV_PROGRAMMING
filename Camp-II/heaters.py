class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i, j = 0, 0
        radius = 0
        while i < len(houses):
            if houses[i] <= heaters[j]:
                radius = max(radius, heaters[j] - houses[i])
                i += 1
            elif j < len(heaters) - 1:
                if houses[i] - heaters[j] > heaters[j+1] - houses[i]:
                    j += 1
                else:
                    radius = max(radius, houses[i] - heaters[j])
                    i += 1
            else:
                radius = max(radius, houses[i] - heaters[j])
                i += 1
        return radius