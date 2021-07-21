'''
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        option =[1,2,3]
        stack = [(0,[])]
        ans = []
        
        def check(s):
            if int(s) <= 255 and len(s) == len(str(int(s))):
                return True
            return False
        
        while stack:
            length, parts = stack.pop()
            if length == 3:
                if sum(parts) < len(s):
                    
                    rest = len(s)-sum(parts)
                    p1 = s[0:parts[0]]
                    
                    
                    p2 = s[parts[0]:parts[0]+parts[1]]
                    
                    p3 = s[parts[0]+parts[1]:parts[0]+parts[1]+parts[2]]
                    
                    p4 = s[-rest:]
                    if check(p1) and check(p2) and check(p3) and  check(p4):
                        ans.append(".".join([p1,p2,p3,p4]))
            else:
                for op in option:
                    stack.append((length+1,parts+[op]))
        
        return ans