class Solution(object):
    def rearrangeCharacters(self, s, target):

        count_s = {}
        count_target = {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in target:
            count_target[ch] = count_target.get(ch, 0) + 1

        ans = float('inf')

        for ch in count_target:
            copies = count_s.get(ch, 0) // count_target[ch]
            ans = min(ans, copies)

        return ans