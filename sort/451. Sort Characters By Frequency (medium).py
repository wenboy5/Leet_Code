'''Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of English letters and digits.
'''

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        l=sorted(((val,key) for val, key in counter.items()), key=lambda x:x[1], reverse= True)
        print(l)
        res = ""
        for val,key in l:
            res+= val*key
        return res


#most_common
class Solution:
    def frequencySort(self, s: str) -> str:

        # Count up the occurances.
        counts = collections.Counter(s)

        # Build up the string builder.
        res = ""
        for letter, freq in counts.most_common():
            # letter * freq makes freq copies of letter.
            # e.g. "a" * 4 -> "aaaa"
            res+=letter * freq
        return res