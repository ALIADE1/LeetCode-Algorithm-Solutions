class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mergee = items1 + items2
        count = defaultdict(int)

        for value, weight in mergee:
            count[value] += weight

        return sorted([[value, weight] for value, weight in count.items()])
