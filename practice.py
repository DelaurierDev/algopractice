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

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        return haystack.index(needle)
    return -1

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
def isSubsequence(self, s, t):
    i = 0
    if len(s) == 0:
        return True
    else:
        for let in t:
            if i == len(s):
                return True
            if let == s[i]:
                i += 1
        if i == len(s):
            return True
    return False

'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

'''
def findDifference( nums1, nums2):
    one = []
    two = []
    map = {}
    for i in nums1:
        if i not in nums2 and i not in map:
            map[i] = 1
    for i in nums2:
        if i not in nums1 and i not in map:
            map[i] = 2
    for key, value in map.items():
        if value == 1:
            one.append(key)
        else:
            two.append(key)
    return [one, two]

print(findDifference([1,2,3,3],[1,1,2,2]))
    
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''

def guessNumber(n):
    low = 1
    high = n
    mid = (low + high) / 2
    while guess(mid) != 0:
        if guess(mid) == 1:
            low = mid + 1
        elif guess(mid) == -1:
            high = mid - 1
        mid = (low + high) / 2
    return mid

'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

def kidsWithCandies(self, candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max = 0
    for val in candies:
        if val > max:
            max = val
    ans = []
    for val in candies:
        if val + extraCandies >= max:
            ans.append(True)
        else:
            ans.append(False)
    return ans

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
def maxProfit(self, prices):
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(currentProfit,max_profit)
        else:
            left = right
        right += 1
    return max_profit

'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

def reverseVowels( s):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    vowels = "aeiouAEIOU"
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
    return ''.join(s)

print(reverseVowels("hello"))

'''
leet code weekly contest 377
'''

def numberGame( nums):
    arr = []
    if len(nums) == 0:
        return []
    while len(nums) != 0:
        a = min(nums)
        nums.remove(a)
        b = min (nums)
        nums.remove(b)
        arr.append(b)
        arr.append(a)
        print(arr)
    return arr
numberGame([2,7,9,6,4,6])

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (i != j and nums[i] + nums[j] == target):
                return [i, j]
        

'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
def isIsomorphic(self, s, t):
    map1 = []
    map2 = []
    for idx in s:
        map1.append(s.index(idx))
    for idx in t:
        map2.append(t.index(idx))
    if map1 == map2:
        return True
    return False

'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
'''
def summaryRanges(nums):
	result = []

	start , end = 0 , 0

	while start < len(nums) and end < len(nums):

		if (end + 1) < len(nums) and nums[end] + 1 == nums[end + 1]:
			end = end + 1
		else:

			if nums[start] == nums[end]:
				result.append(str(nums[start]))
				start = start + 1
				end = end + 1

			else:
				result.append(str(nums[start]) + '->' + str(nums[end]))
				end = end + 1
				start = end

	return result
        

print(summaryRanges([0,1,2,4,5,7]))

'''
Given a roman numeral, convert it to an integer.
'''

def romanToInt(self, s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i, j = 0, 0
    n = len(nums)
    while i < n and j < n:
        if nums[i] != 0:
            i += 1
            continue
        if nums[j] == 0:
            j += 1
            continue
        if (i < j):
            nums[i] = nums[j]
            nums[j] = 0
        j += 1
