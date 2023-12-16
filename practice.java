
import java.util.HashMap;
class Practice{
    public static void main(String[] args){
    }

/*Leetcode 88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

*/

    public void merge(int[] nums1, int m, int[] nums2, int n){
        // My solution
        // Initialize a variable that keeps track of where we are in the array
        int p = m + n - 1;
        // Initialize 2 pointers that start at the end of where the elements begin in each array
        int p1 = m - 1;
        int p2 = n - 1;

        //then we check which values are bigger and inster them into the array 
        while(p1>=0 && p2>=0){
            if(nums1[p1] > nums2[p2]){
                nums1[p] = nums1[p1];
                p--;
                p1--;
            } else {
                nums1[p] = nums2[p2];
                p--;
                p2--;
            }
        }
        
        //implement this while loop for edge cases where nums1 is empty
        while(p2>=0){
            nums1[p] = nums2[p2];
            p--;
            p2--;
        }

    }

    /*Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k. */
    public int removeElement(int[] nums, int val) {
        //initialize k to count how many are not equal to val
        int k = 0;
        //initialize two pointers, one to check if the val in nums is equal to val, one to keep track of where to swap;
        int t = nums.length - 1;
        int p = nums.length - 1;
        //Iterate throught the array
        while(p >= 0){
            //if where p is in the array = val swap nums[p] and nums[t]
            if(nums[p] == val){
                nums[p] = nums[t];
                nums[t] = val;
                p --;
                t --;
            }
            //if not increment k by one and decrease p
            else{
                p --;
                k ++;
            }
        }
        return k;
    }


/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
 */

public int removeDuplicates(int[] nums) {
    int k = 1;
    int currentValue = nums[0];
    int p1 = 1;
    int p2 = 1;
    while(p2 < nums.length){
        if(nums[p2] == currentValue){
            p2++;
        }
        else if(nums[p2] != currentValue){
            k++;
            currentValue = nums[p2];
            nums[p1] = currentValue;
            p2++;
            p1++;
        }
    }
    return k;
    }


/*Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. */

public boolean isAnagram(String s, String t) {
    //if the lengths are the same they cant be anagrams
    if (s.length() != t.length()) {
        return false;
    }
    //create an array to keep track of the frequencies of the letters
    int[] freq = new int[26];
    // iterate through the array
    for (int i = 0; i < s.length(); i++) {
        //add one for every time the char shows up in s
        freq[s.charAt(i) - 'a']++;
        //subtract one for everytime the char shows up in t
        freq[t.charAt(i) - 'a']--;
    }
    // if they are anagrams, every value in freq array should be zero
    for (int i = 0; i < freq.length; i++) {
        if (freq[i] != 0) {
            return false;
        }
    }
    
    return true;
}
/*A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. */
public boolean isPalindrome(String s) {
    String str = "";
    for(int i = 0; i < s.length(); i++){
        char c = s.charAt(i);
        if((c >= 'a' && c <= 'z') ||
        (c >= 'A' && c <= 'Z') ||
        (c >= '0' && c <= '9')){
            str += Character.toLowerCase(c);
        }
    }
    System.out.println(str);
    String rev = "";
    for(int i = str.length() - 1; i >=0; i --){
        rev += str.charAt(i);
    }
    if(rev == str){
        return true;
    }
    return false;
        
}

/* Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.*/
public int[] twoSum(int[] numbers, int target) {
    int left = 0;
    int right = numbers.length - 1;
    int tmp;
    while (left < right)
    {
        if (numbers[left] + numbers[right] == target) break;
        tmp = target - numbers[right];
        while (numbers[left] < tmp) left++;
        if (numbers[left] + numbers[right] == target) break;
        tmp = target - numbers[left];
        while (numbers[right] > tmp) right--;
    }
    return new int[]{left + 1, right + 1};
}

/* Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.*/
public int strStr(String haystack, String needle) {
    return haystack.indexOf(needle);
}

/* Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).*/
public boolean isSubsequence(String s, String t) {
        int currentIndex = 0;
        int p1 = 0;
        while(t.indexOf(s.charAt(p1), currentIndex) >= 0){
            p1++;
            currentIndex = t.indexOf(s.charAt(p1), currentIndex) + 1;
        }
        if(p1 == s.length() - 1){
            return true;
        }
        return false;
}
}
