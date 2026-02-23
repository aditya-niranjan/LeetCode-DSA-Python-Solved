class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.size();
        
        // Quick impossible case check
        if (n < k || n - k + 1 < (1 << k)) 
            return false;

        int total = 1 << k;
        vector<bool> seen(total, false);

        int mask = 0;
        int remaining = total;

        for (int i = 0; i < n; ++i) {
            // Build rolling k-bit number
            mask = ((mask << 1) & (total - 1)) | (s[i] - '0');

            if (i >= k - 1 && !seen[mask]) {
                seen[mask] = true;
                if (--remaining == 0)
                    return true;   // All codes found
            }
        }

        return false;
    }
};