# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = 2 * len(s) - 1
        current_length = 1
        centres = [None]*(n)
        # so e.g. if "between s[1] and s[2] is the centre"
        # then centre[3] is where the state of the palindrome is kept
        ran_out_of_odd = False
        ran_out_of_even = False
        longest_thus_far = ''
        while current_length <= len(s):
            if current_length % 2 == 1 and not ran_out_of_odd:
                # Odd length palindromes
                found_any = False
                # Looking at each of the available centres (at current length)
                for i in ((current_length//2), len(s) - (current_length//2)):
                    if current_length == 1:
                        centres[i*2] = True
                    else:
                        centres[i*2] = centres[i*2] and s[i - (current_length//2)] == s[i + (current_length//2)]
                    if centres[i*2]:
                        found_any = True
                        longest_thus_far = s[i-(current_length//2):i+(current_length//2)]
                        break
                if not found_any:
                    ran_out_of_odd = True
            elif not ran_out_of_even:
                found_any = False
                for i in range(0, len(s) - 1):
                    centre_index = (i+0.5)*2
                    if current_length == 2:
                        centres[centre_index] = 
                    if s[i+1-current_length/2] == s[i+current_length/2]:
                        if centres[centre_index]:


            else:
                break
            current_length += 1


    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     longest_thus_far = ''
    #     # Odd Palindromes
    #     first_layer = [None]*(n)
    #     for i in range(n):
    #         first_layer[i] = True
    #         longest_thus_far = s[i:i+1]
    #     last_layer = first_layer
    #     for p in range(0, n//2+1):
    #         any_found = False
    #         this_layer = [None]*n
    #         for i in range(p,n-p):
    #             # Is it still a palindrome centered at i?
    #             is_palin = last_layer[i] and s[i-p] == s[i+p]
    #             this_layer[i] = is_palin
    #             if is_palin:
    #                 longest_thus_far = s[i-p:i+p+1] if 2*p+1 > len(longest_thus_far) else longest_thus_far
    #                 any_found = True
    #         last_layer = this_layer
    #         if not any_found:
    #             break
    #     # Even Palindromes
    #     first_layer = this_layer = [None]*(n-1)
    #     for i in range(n-1):
    #         first_layer[i] = s[i] == s[i+1]
    #         if first_layer[i] and len(longest_thus_far) < 2:
    #             longest_thus_far = s[i:i+2]
    #     last_layer = first_layer
    #     for p in range(1, n//2):
    #         any_found = False
    #         this_layer = [None]*(n-1)
    #         for i in range(p, n-p):
    #             # Is it still a palindrome centered at i+0.5?
    #             print(i)
    #             print(p)
    #             print(len(s))
    #             is_same = s[i-p] == s[i+p+1]
                
    #             is_palin = last_layer[i] and is_same
    #             this_layer[i] = is_palin
    #             if is_palin:
    #                 longest_thus_far = s[i-p:i+p+2] if 2*p+2 > len(longest_thus_far) else longest_thus_far
    #                 any_found = True
    #         last_layer = this_layer
    #         if not any_found:
    #             break
    #     return longest_thus_far