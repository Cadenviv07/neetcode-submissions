class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dupe = new HashSet<>();

        for(int num: nums){

            if(dupe.add(num) == false){

                return true;

            }
        }
        return false;
    }
}