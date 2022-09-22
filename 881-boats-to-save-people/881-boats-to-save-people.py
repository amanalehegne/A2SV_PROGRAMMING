class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat, l, r = 0, 0, len(people) - 1
        people.sort()
        while l <= r:
            # The Smallest Weight person has the most option and the Highest Weight person has the least
            # If their weight is less or equal to limit, they will go together.
            # If their weight is more than the max, the Maximum weight person has l=no option left to go with so goes alone
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            # Now the Maximum weight person has changed, so we checked and repeat the process
            else:
                r -= 1
            boat += 1
        return boat
