class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m != 0 and n != 0:
            for i in range(m):
                if nums1[i] > nums2[0]:
                    val = nums2[0]
                    nums2[0] = nums1[i]
                    nums1[i] = val

                    nums2.sort()

            p = 0
            for j in range(m, m + n):
                nums1[j] = nums2[p]
                p += 1 

        elif m == 0 and n != 0:
            for _ in range(n):
                nums1.pop(0)
            for num in nums2:
                nums1.append(num)
