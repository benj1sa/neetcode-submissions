class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_height = []
        for i, name in enumerate(names):
            names_height.append((name, heights[i]))

        sorted_heights = sorted(names_height, key=lambda item: item[1], reverse=True)

        names = []
        for name, height in sorted_heights:
            names.append(name)
        
        return names