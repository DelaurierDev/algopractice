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
    

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

def removeDuplicates(self, nums):
    k = 1
    currVal = nums[0]
    p1 = 1
    p2 = 1
    while(p2 < len(nums)):
        if(nums[p2] == currVal):
            p2 += 1
        elif(nums[p2] != currVal):
            currVal = nums[p2]
            nums[p1] = currVal
            p2 += 1
            p1 += 1
            k += 1
    return k

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    dict = {}
    for char in s:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    for char in t:
        if char in dict:
            dict[char] = dict[char] - 1
        else:
            dict[char] = 1
    for value in dict.values():
        if value != 0:
            return False

    return True


print(isAnagram("hello", "yo"))

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome( s):
    """
    :type s: str
    :rtype: bool
    """
    b=""
    i=0
    
    for char in s:
        if char.isalpha() or char.isnumeric():
            b += char.lower()
    print(b)
    j=len(b) - 1
    while(i <= j):

        if(b[i] != b[j]):
            return False
        i += 1
        j -= 1 

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))


'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1
    while(left < right):
        if numbers[left] + numbers[right] == target:
            return [left+1, right +1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1