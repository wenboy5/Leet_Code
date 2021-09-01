'''
Count the number of prime numbers less than a non-negative number, n.


Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2

#time limit exceeded
class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        if n <= 2:
            return ans
        
        def check_prime(i):
            for j in range(2,int(i/2)+1):
                if i%j == 0:
                    return False
            return True
        
        
        #print("keke",check_prime(3))  
        
        
        for i in range(2,n):
            if check_prime(i):
                ans += 1
                #print(i)
        return ans
