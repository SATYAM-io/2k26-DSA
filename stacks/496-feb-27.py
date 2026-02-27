#  496. Next Greater Element I

#  class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         n1 , n2 = len(nums1),len(nums2)
#         ans = [-1]*n1
#         for i in range(0,n1):
#             j = 0
#             while nums2[j] != nums1[i]:
#                 j+=1
#             j+=1
#             while j < n2:
#                 if nums2[j] > nums1[i]:
#                     ans[i] = nums2[j]
#                     break
#                 j +=1
#         return ans

#  this was brute force approach with time complexity O(n1*n2) and space complexity O(n1)

        