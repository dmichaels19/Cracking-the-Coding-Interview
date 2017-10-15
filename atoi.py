class Solution(object):
    def myAtoi(self, str):
        """
implement Python's int() function for int: string -> integer
"""
        if str == "":
            return 0

        negate = False
        sum = 0

        str = str.strip(" ")

        i = 0
        if str[0] == '+':
            i = 1
        elif str[0] == '-':
            i = 1
            negate = True

        ord0 = ord("0")
        ord9 = ord("9")

        len_s = len(str)
        while (i < len_s):
            char = str[i]
            if ord(char) >= ord0 and ord(char) <= ord9:
                sum += (ord(char) - ord('0')) * 10 ** (len(str) - i - 1)
            else:
                sum = int(sum / (10 ** (len_s - i)))
                break
            i += 1
        sum = sum if not negate else (sum * -1)

        if sum > 2147483647:
            sum = 2147483647
        elif sum < -2147483648:
            sum = -2147483648

        return sum

print(Solution().myAtoi("+1"))

print(Solution().myAtoi("    010"))

