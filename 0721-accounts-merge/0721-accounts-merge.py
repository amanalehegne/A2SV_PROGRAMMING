from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep = dict()
        size = dict()

        for account in accounts:
            length = len(account)
            for idx in range(1, length):
                pair = (account[idx], account[0])
                rep[pair] = pair
                size[pair] = 1

        def find(rep, pair):
            if pair == rep[pair]:
                return pair
            rep[pair] = find(rep, rep[pair])
            return rep[pair]

        def union(rep, size, pair1, pair2):
            pair1 = find(rep, pair1)
            pair2 = find(rep, pair2)

            if pair1 == pair2:
                return
            size1, size2 = size[pair1], size[pair2]
            if size1 > size2:
                pair1, pair2 = pair2, pair1

            rep[pair1] = pair2
            size[pair2] += size[pair1]

        for account in accounts:
            length = len(account)
            base = (account[1], account[0])
            for idx in range(2, length):
                union(rep, size, base, (account[idx], account[0]))

        merged = dict()
        for account in accounts:
            length = len(account)
            for idx in range(1, length):
                email = account[idx]
                root = find(rep, (email, account[0]))
                if root not in merged:
                    merged[root] = set()
                merged[root].add(email)

        res = []
        for root in merged:
            emails = merged.get(root)
            res.append([root[1]] + sorted(emails))


        return res
