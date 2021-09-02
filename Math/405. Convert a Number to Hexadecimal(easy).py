'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
'''

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
            
        res = ""
        letter = "0123456789abcdef"
        while num > 0:
            res = letter[num % 16] + res
            num //= 16
        return res

class Solution:
    def toHex(self, num: int) -> str:
        num_to_hex = {10:"a",
                      11:"b",
                      12:"c",
                      13:"d",
                      14:"e",
                      15:"f",
                     }
        convert =    {"a":10,
                      "b":11,
                      "c":12,
                      "d":13,
                      "e":14,
                      "f":15,
                     }
        flag = False
        
        if num == 0:
            return "0"
        
        if num < 0:
            flag = True
            num = -num
        
        res = ""
        
        while num >= 16:
            reminder = num%16
            if reminder > 9:
                reminder = num_to_hex[reminder]
            res += str(reminder)
            num = num//16 #quotient
        res += str(num) if num <= 9 else num_to_hex[num]
        
        res = res[::-1]
        
        new_res = ["0" for _ in range(8)]
        check = False
        if flag:
            for i in range(-1,-len(res)-1,-1):
                new_res[i] = res[i]
            for i in range(-1,-len(new_res)-1,-1):
                
                if new_res[i] in convert:
                    new_res[i] = 15-convert[new_res[i]]
                else:
                    new_res[i] = 15 - int(new_res[i])
                if i == -1 or check:
                    new_res[i] += 1
                    if new_res[i] == 16:
                        check = True
                        new_res[i] = "0"
                    elif new_res[i] > 9:
                        new_res[i] = num_to_hex[new_res[i]]
                        check = False
                    else:
                        check = False
                        new_res[i] = str(new_res[i])
                else:
                    if new_res[i] > 9:
                        new_res[i] = num_to_hex[new_res[i]]
                    else:
                        new_res[i] = str(new_res[i])
            res = "".join(new_res)
            
        while len(res)!=1 and res[0] == 0:
            res = res[1:]
        return res