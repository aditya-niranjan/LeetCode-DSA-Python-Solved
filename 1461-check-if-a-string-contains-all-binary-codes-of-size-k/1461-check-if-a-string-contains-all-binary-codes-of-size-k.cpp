class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.size();
        int total = 1 << k;

        // Impossible check
        if (n < k || n - k + 1 < total) 
            return false;

        vector<char> seen(total, 0);

        int mask = 0;
        int needed = total;
        int limit = total - 1;

        for (int i = 0; i < n; ++i) {
            mask = ((mask << 1) & limit) | (s[i] & 1);

            if (i >= k - 1) {
                if (!seen[mask]) {
                    seen[mask] = 1;
                    if (--needed == 0)
                        return true;
                }
            }
        }

        return false;
    }
};