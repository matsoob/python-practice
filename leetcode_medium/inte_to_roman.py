# https://leetcode.com/problems/integer-to-roman/

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    mapping = {
        0: {
            'one': 'I',
            'five': 'V'
        },
        1: {
            'one': 'X',
            'five': 'L'
        },
        2: {
            'one': 'C',
            'five': 'D'
        },
        3: {
            'one': 'M',
            'five': '?'
        },  
    }
    def intToRoman(self, num: int) -> str:
        # 2 2 3 -> CC XX III
        # 4 6 9 -> CD LX IX
        # 5 1 0 -> D X 
        
        def translate(digit: int, power: int) -> str:
            if digit <= 3:
                return self.mapping[power]['one']*digit
            if digit == 4:
                return self.mapping[power]['one'] + self.mapping[power]['five'] 
            if digit < 9:
                return self.mapping[power]['five'] + self.mapping[power]['one']*(digit%5)
            if digit == 9:
                return self.mapping[power]['one'] + self.mapping[power+1]['one']

        computed = list()
        current_ten_pow = 0
        while num != 0:
            current_digit = num % 10
            
            computed.append(translate(current_digit, current_ten_pow))
            num = num // 10
            current_ten_pow +=1
        computed.reverse()
        return ''.join(computed)




if __name__ == '__main__':
    sol = Solution()
    test_input = 123
    print(sol.intToRoman(test_input))
    print(sol.intToRoman(1994))