class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        total = 1 << k
        
        # Quick impossible check
        if n < k or n - k + 1 < total:
            return False
        
        seen = [0] * total
        mask = 0
        needed = total
        limit = total - 1
        
        for i in range(n):
            # Build rolling k-bit integer
            mask = ((mask << 1) & limit) | (s[i] == '1')
            
            if i >= k - 1:
                if not seen[mask]:
                    seen[mask] = 1
                    needed -= 1
                    if needed == 0:
                        return True
        
        return False