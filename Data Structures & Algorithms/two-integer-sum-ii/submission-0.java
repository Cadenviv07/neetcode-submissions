class Solution {
    public int[] twoSum(int[] nums, int target) {
        int smallest = 0;
        int largest = nums.length - 1; 

        while(smallest < largest){
               int sum = nums[smallest] + nums[largest];

            if (sum == target) {
                return new int[]{smallest + 1, largest + 1};
            } else if (sum > target) {
                largest--;
            } else {
                smallest++;
            }
        }
        return new int[]{-1, -1};
    }
}
