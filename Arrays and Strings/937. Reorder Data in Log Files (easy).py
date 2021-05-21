'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        #digit_logs = [log for log in logs if log.split()[1][0] in "0123456789"]
        #letter_logs = [log for log in logs if log not in digit_logs]
        s="0123456789"
        digit= []
        letter = []
        for i in logs:
            iden = i.split(" ")[0]
            rest = "".join(i.split(" ")[1:])
            if rest[0] in s:
                digit.append(i)
            else:
                letter.append(i)
        #given that Python sort is stable
        #first, sort the letter_logs based on the identifiers so that they can remain in order of the identifiers 
        #if the contents are identical
        #second, sort the letter_logs based on the contents
        
        letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        
        #append the digit_logs and return the result
        return letter + digit