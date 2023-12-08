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

majorityElement([2,2,1,1,1,2,2])