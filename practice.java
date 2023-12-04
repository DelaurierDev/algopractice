

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

}