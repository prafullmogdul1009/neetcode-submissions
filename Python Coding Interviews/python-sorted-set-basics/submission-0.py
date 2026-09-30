from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    srt_set = SortedSet(sorted_set)
    for num in nums1:
        srt_set.add(num)
        
    for num in nums2:
        if ( num in srt_set):
            srt_set.remove(num)

    list(srt_set)
    lt =[]
    for i in range(3):
        lt.append(srt_set[i])

    return lt
# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
