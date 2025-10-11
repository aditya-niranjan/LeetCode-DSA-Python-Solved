class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        roman = ""

        for i in range(len(values)):
            times = num // values[i]
            if times:
                roman += symbols[i] * times
                num -= values[i] * times
        return roman

s1 =  Solution()
print(s1.intToRoman(3749))

        