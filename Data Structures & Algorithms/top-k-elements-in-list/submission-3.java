class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 1. Write nums into a frequency table:
        HashMap<Integer, Integer> freq = new HashMap<>();
        List<Integer>[] buckets = new ArrayList[nums.length + 1];
        int[] result = new int[k];

        for (int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (Integer num : nums) {
            if (freq.get(num) == null) freq.put(num, 1);
            else freq.put(num, freq.get(num) + 1); 
        }

        // 2. Write freq into a bucket sort array
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            buckets[entry.getValue()].add(entry.getKey());
        }

        // 3. Run back through buckets
        int i = buckets.length - 1;
        int j = 0;
        while (i >= 0 && j < k) {
            for (Integer num : buckets[i]) {
                result[j] = num;
                j++;
            }
            i--;
        }

        System.out.println(freq.toString());
        return result;
    }
}
