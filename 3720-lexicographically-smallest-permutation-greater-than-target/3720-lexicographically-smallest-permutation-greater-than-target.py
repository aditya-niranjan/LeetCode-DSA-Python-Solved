class Solution(object):
    def lexGreaterPermutation(self, s, target):

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(target)

        # Match target from left to right
        i = 0

        while i < n:

            idx = ord(target[i]) - ord('a')

            if count[idx] > 0:
                count[idx] -= 1
                i += 1

            else:
                break

        # Try to make the answer greater at position i
        # First, try the current position.
        if i < n:

            idx = ord(target[i]) - ord('a')

            for j in range(idx + 1, 26):

                if count[j] > 0:

                    count[j] -= 1

                    ans = target[:i] + chr(j + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans

        # Current position didn't work.
        # Go backwards through the matched prefix.
        for j in range(i - 1, -1, -1):

            idx = ord(target[j]) - ord('a')

            # Put target[j] back
            count[idx] += 1

            # Try a character slightly bigger
            for x in range(idx + 1, 26):

                if count[x] > 0:

                    count[x] -= 1

                    ans = target[:j] + chr(x + ord('a'))

                    # Remaining characters in smallest order
                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans

        return ""