class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        count = 0
        people.sort()
        while l <= r:
            if l < r:
                weight_check = people[l] + people[r]
            else:
                weight_check = people[l]
            
            if weight_check <= limit:
                l += 1
                r -= 1
            elif weight_check > limit:
                r -= 1
                
            count += 1
        return count