'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
'''

from collections import defaultdict
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        
        """
        newstr = re.split(r'\W',paragraph.lower())
        #print(newstr)
        res = Counter(filter(lambda x: (x!='') and (x not in banned), newstr))
        return res.most_common(1)[0][0]

from collections import defaultdict
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        
        """
        string = re.sub(r'[^\w\s]',' ',paragraph)
        
        print(string)
        d = defaultdict(int)
        for word in string.split(" "):
            word = word.strip().lower()
            print(word)
            if word != "":
                d[word] += 1 
            
        count = 0
        res = ""
        for k, v in d.items():
            if k not in banned:
                if v > count:
                    count = v 
                    res = k
        print(count)
        print(res)
        print(d)
        return res