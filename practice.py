#LEETCODE 88. Merge Sorted Array

#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(self, nums1, m, nums2, n):
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1

    while(p1 >= 0 and p2 >= 0):
        if(nums1[p1] > nums2[p2]):
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
    while(p2>=0):
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#Return k.

def removeElement(self, nums, val):
    while(val in nums):
        nums.remove(val)
    return len(nums)
    