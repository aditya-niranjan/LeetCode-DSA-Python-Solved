class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        count = 0
        ans = float('inf')
        st = ""

        for right in range(len(s)):

            if s[right] == "1":
                count += 1

            while count == k:

                current = s[left:right + 1]
                length = right - left + 1

                if length < ans:
                    ans = length
                    st = current

                elif length == ans and current < st:
                    st = current

                if s[left] == "1":
                    count -= 1

                left += 1

        return st