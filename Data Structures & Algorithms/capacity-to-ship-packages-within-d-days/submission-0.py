class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = min_capacity =  l * len(weights)

        while l <= r:
            capacity = l + (r - l) // 2

            load = 0
            capacity_days = 1
            for w in weights:
                if load + w > capacity:
                    capacity_days += 1
                    load = w
                else:
                    load += w

            if capacity_days <= days:
                min_capacity = min(min_capacity, capacity)
                r = capacity - 1
            else:
                l = capacity + 1
        
        return min_capacity