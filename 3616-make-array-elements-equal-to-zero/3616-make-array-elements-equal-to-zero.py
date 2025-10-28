class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        zeros = [i for i in range(n) if nums[i] == 0]

        def simulate(start, direction):
            arr = nums[:]  # copy original
            curr = start
            dir = direction

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir = -dir  # reverse direction
                    curr += dir

            return all(x == 0 for x in arr)

        valid = 0
        for z in zeros:
            if simulate(z, 1):  # right
                valid += 1
            if simulate(z, -1):  # left
                valid += 1

        return valid
