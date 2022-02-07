from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        print(m)
        print(n)
        i = 1
        j = 1
        s = 1
        while s < (n + m):
            k = nums1[(i * -1) - m]
            if k < nums2[j * -1]:
                nums1[s * -1] = nums2[j * -1]
                j = j + 1
            else:
                nums1[s * -1] = nums1[(i * -1) - m]
                i = i + 1
            s = s + 1
        print(nums1)



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution=Solution
solution.merge(solution,nums1, m, nums2, 3)



# i = 0
# j = 0
# k = 0
#
# while i < m and j < n:
#     if nums1[i] < nums2[j]:
#         arr3[k] = arr1[i]
#         k = k + 1
# #         if arr1[i] < arr2[j]:
#             arr3[k] = arr1[i]
#             k = k + 1
#             i = i + 1
#         else:
#             arr3[k] = arr2[j]
#             k = k + 1
#             j = j + 1
#
#     # Store remaining elements
#     # of first array
#     while i < n1:
#         arr3[k] = arr1[i];
#         k = k + 1
#         i = i + 1
#
#     # Store remaining elements
#     # of second array
#     while j < n2:
#         arr3[k] = arr2[j];
#         k = k + 1
#         j = j + 1
#     print("Array after merging")
#     for i in range(n1 + n2):
#         print(str(arr3[i]), end=" ")
#
#
# # Driver code
# arr1 = [1, 3, 5, 7]
# n1 = len(arr1)
#
# arr2 = [2, 4, 6, 8]
# n2 = len(arr2)
# mergeArrays(arr1, arr2, n1, n2);
#
# # This code is contributed
# # by ChitraNayal