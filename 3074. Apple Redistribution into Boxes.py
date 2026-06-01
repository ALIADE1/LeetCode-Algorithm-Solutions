class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_app = sum(apple)
        summ_cap, i = 0, 0
        capacity = sorted(capacity, reverse=True)

        for x in capacity:
            if summ_cap >= total_app:
                return i
            else:
                i+=1
                summ_cap+=x

        return len(capacity)
