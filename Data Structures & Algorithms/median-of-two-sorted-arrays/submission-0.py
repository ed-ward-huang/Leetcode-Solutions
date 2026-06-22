class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ## merge two arrays, then find median: O(n + m)

        ## median: middle value -> same number of elements larger and smaller ->
        ## median of combined sorted array
        ## binary search to find median element


        # [16 -> up, 5 elements] 10 // 2 = 5, 5 - 3 = 2
        # [5 6 8 14 16]

        
        half = (len(nums1) + len(nums2)) // 2

        left, right = 0, len(nums1)

        ## do binary search
        while left <= right:
            ## 2 partitions, p1 for nums1, p2 for nums2
            ## for both partitions, all elements to the left would be considered
            ## the smaller half of the merged array, all elements to the right would be larger half

            ## check for validity and if we should search to the left or nums1 for our new set or partitions
            ## can calculate second partition from the first partition, p2 = half - p1

            p1 = (left + right) // 2
            p2 = half - p1

            ## check surroundings to determine validity
            ## p1_left element left of p1
            ## p1_left <= p2_right
            ## p2_left <= p1_right

            p1_left = nums1[p1 - 1] if p1 > 0 else float("-inf")
            p1_right = nums1[p1] if p1 < len(nums1) else float("inf")

            p2_left = nums2[p2 - 1] if p2 > 0 else float("-inf")
            p2_right = nums2[p2] if p2 < len(nums2) else float("inf")     


            ## verify correct partition
            if p1_left <= p2_right and p2_left <= p1_right:
                ## return median
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (
                        max(p1_left, p2_left) +
                        min(p1_right, p2_right)
                    ) / 2
                else:
                    return min(p1_right, p2_right)

            elif p1_left > p2_right:
                right = p1 - 1
            else:
                left = p1 + 1
        










