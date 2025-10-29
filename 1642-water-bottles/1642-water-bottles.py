class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange   # how many new bottles we get
            total_drunk += new_bottles          # drink them
            empty = empty % numExchange + new_bottles  # remaining + new empties

        return total_drunk
