class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;

        for (int num : nums) {
            if (!map.containsKey(num)) {
                int left = map.getOrDefault(num - 1, 0);
                int right = map.getOrDefault(num + 1, 0);

                int length = left + right + 1;
                map.put(num, length);

                max = Math.max(max, length);

                // Update sequence boundaries
                map.put(num - left, length);
                map.put(num + right, length);
            }
        }

        return max;
    }
}
