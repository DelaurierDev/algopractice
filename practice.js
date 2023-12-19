/*You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 */

var merge = function(nums1, m, nums2, n) {
    var p = m + n - 1;
    // Initialize 2 pointers that start at the end of where the elements begin in each array
    var p1 = m - 1;
    var p2 = n - 1;

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
};

/*Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.*/ 

var removeElement = function(nums, val) {
            //initialize k to count how many are not equal to val
            let k = 0;
            //initialize two pointers, one to check if the val in nums is equal to val, one to keep track of where to swap;
            let t = nums.length - 1;
            let p = nums.length - 1;
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
};

/*Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.*/

var removeDuplicates = function(nums) {
    let k = 1;
    let currentValue = nums[0]
    let p1 = 1;
    let p2 = 1;
    while(p2 < nums.length){
        if(nums[p2] == currentValue){
            p2++
        }
        else if(nums[p2] != currentValue){
            k++
            currentValue = nums[p2]
            nums[p1] = currentValue
            p2++
            p1++
        }
    }
    return k
};  

/*Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.*/

var majorityElement = function(nums) {
    const map = new Map()
    for(let i = 0; i < nums.length; i++){
        let key = nums[i]
        if(map.get(key) >= 1){
            val =map.get(key) 
            val++
            map.set(key, val)
        }
        else{
            map.set(key, 1)
        }
    }

    for (let [key, value] of  map.entries()) {
        if(value >= nums.length / 2){
            return key
        }
    }

};

/*Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.*/

var canConstruct = function(ransomNote, magazine) {
    const r = new Map()
    const m = new Map()

    for(let i = 0; i < ransomNote.length; i++){
        let key = ransomNote[i]
        if(r.get(key) >= 1){

            let val = r.get(ransomNote[i]) + 1
            r.set(key, val)
                }
        else{
            r.set(key, 1)
            m.set(key, 0)
        }

    }
    for(let i = 0; i < magazine.length; i++){
        let key = magazine[i]
        if(m.get(key) >= 0){
            let val = m.get(magazine[i]) + 1
            m.set(key, val)            
        }
        else{
            m.set(key, 1)
        }
    }
    console.log(m)
    for (let [key, value] of  r.entries()) {
        if(m.get(key) < value || m.get(key) == undefined){
            return false
        }
    }
    return true

};

console.log(canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))

/*Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.*/

var isAnagram = function(s, t) {
    const one = new Map()
    const two = new Map()
    if(s.length != t.length){
        return false
    }
    for(let i = 0; i < s.length; i++){
        let key = s[i]
        if(one.get(key) >= 0){
            let val = one.get(s[i]) + 1
            one.set(key, val)            
        }
        else{
            one.set(key, 1)
            two.set(key, 0)
        }
    }
    for(let i = 0; i < t.length; i++){
        let key = t[i]
        if(two.get(key) >= 1){

            let val = two.get(t[i]) + 1
            two.set(key, val)
                }
        else{
            two.set(key, 1)
        }

    }    
    for (let [key, value] of  one.entries()) {
        if(two.get(key) != value ){
            return false
        }
    }
    return true

};

isAnagram("a", "ab")

/*A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.*/
var isPalindrome = function(s) {
    /*var b = '';
    for (var i = 0; i < s.length; i++) {
        console.log(s[i])
        if (s[i].match(/^[a-zA-Z0-9]/)) {
            b += s[i].toLowerCase()
        }
    }
    console.log(b)
    let back = b.length - 1
    let front = 0
    while(back >= front){
        if(b[back] != b[front]){
            return false
        }
        back --
        front ++
    }
    return true*/
    let str = s.replace(/[^a-z0-9]/gi, '').toLowerCase();
    let rev = str.split("").reverse().join("");
    return (str == rev) ? true : false;
};

console.log(isPalindrome("0p"))

/* Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.*/

var twoSum = function(numbers, target) {
    let ans =[];
    for(var p1 = 0;p1 <= numbers.length - 1; p1 ++){
        let p2 = p1 + 1
        while(p2 < numbers.length){
            if(numbers[p1] + numbers[p2] == target){
                ans[0] = p1 + 1
                ans[1] = p2 + 1
                return ans
            }
            else{ p2 ++ }
        }
        
    }
};

console.log(twoSum([5,2575], 100))

/*Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. */
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle)
};


/* Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).*/

var isSubsequence = function(s, t) {
    let j = 0
        for(let i = 0; i < t.length; i++){
            if(s[j] == t[i]){
                j++
            }
        }            
        if(j == s.length  || s.length == 0){
            return true
                }
    return false
};

console.log(isSubsequence("axc", "ahbgdc"))

/* Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.*/

var findDifference = function(nums1, nums2) {
    const a = new Set(nums1)
    const b = new Set(nums2)
    for (const num of a){
        if(b.has(num)){
            a.delete(num)
            b.delete(num)
        }
    }
    return [Array.from(a), Array.from(b)]
};

console.log(findDifference([1,2,3,3],[1,1,2,2]))