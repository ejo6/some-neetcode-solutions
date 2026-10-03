class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> letters = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (!letters.containsKey(s.charAt(i))) {
                letters.put(s.charAt(i), 1);
            } else {
                letters.put(s.charAt(i), letters.get(s.charAt(i)) + 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            if (!letters.containsKey(t.charAt(i))) {
                return false;
            } else {
                letters.put(t.charAt(i), letters.get(t.charAt(i)) - 1);
                if (letters.get(t.charAt(i)) < 0) {
                    return false;
                }
            }
        }

        for (Integer value : letters.values()) {
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
}

