class Solution:

    def lexPalindromicPermutation(self, s, target):

        n = len(s)

        # left[i] = how many copies of character i
        # are available for the two symmetric positions
        left = [0] * 26

        for ch in s:
            left[ord(ch) - ord('a')] += 1

        # Find the middle character, if any
        middle = ""

        for i in range(26):
            if left[i] % 2 == 1:

                # More than one odd count -> impossible
                if middle != "":
                    return ""

                middle = chr(ord('a') + i)

                # Use this odd character as the middle
                left[i] -= 1

        # ------------------------------------------------
        # Assume the answer has the SAME left half
        # as target.
        #
        # Consume two copies of every target-left
        # character because palindrome needs it on
        # both sides.
        # ------------------------------------------------

        for i in range(n // 2):
            idx = ord(target[i]) - ord('a')
            left[idx] -= 2

        # Check whether all counts are still valid
        possible = True

        for x in left:
            if x < 0:
                possible = False
                break

        # ------------------------------------------------
        # Case 1:
        # We can make the left half exactly equal
        # to target's left half.
        #
        # Then compare the RIGHT half.
        #
        # Example:
        # s = "aac"
        # target = "abb"
        #
        # left = "a"
        # middle = "c"
        # palindrome = "aca"
        #
        # Left halves are equal ("a"),
        # so we must compare "ca" with "bb".
        # ------------------------------------------------

        if possible:

            left_part = target[:n // 2]

            right_part = middle + left_part[::-1]

            if right_part > target[n // 2:]:

                return left_part + right_part

        # ------------------------------------------------
        # Case 2:
        #
        # We need to make the answer GREATER by changing
        # one character in the left half.
        #
        # Start from the RIGHTMOST position.
        #
        # Why?
        #
        # Changing a later position keeps the answer
        # as small as possible.
        # ------------------------------------------------

        for i in range(n // 2 - 1, -1, -1):

            idx = ord(target[i]) - ord('a')

            # Put back the two copies that were used
            left[idx] += 2

            # If the prefix before i cannot be formed,
            # we cannot use this position.
            possible = True

            for x in left:
                if x < 0:
                    possible = False
                    break

            if not possible:
                continue

            # Try the smallest character greater than target[i]
            for bigger in range(idx + 1, 26):

                if left[bigger] >= 2:

                    # Use this character on BOTH sides
                    left[bigger] -= 2

                    # Prefix stays equal to target
                    ans = list(target[:i])

                    # Increase position i
                    ans.append(chr(ord('a') + bigger))

                    # Fill remaining left-half positions
                    # with the smallest possible characters
                    for c in range(26):

                        while left[c] >= 2:

                            ans.append(chr(ord('a') + c))
                            left[c] -= 2

                    # We now have the complete left half
                    left_part = ''.join(ans)

                    # Mirror it
                    right_part = left_part[::-1]

                    return left_part + middle + right_part

        return ""