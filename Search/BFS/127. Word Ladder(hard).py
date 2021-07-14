class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        wordList = set(wordList)
        if endWord not in wordList: return 0
        
        l, s1, s2 = len(beginWord), {beginWord}, {endWord}
        wordList.remove(endWord)
        level = 0

        while s1 and s2:
            level += 1
            s = set()
            if len(s1) > len(s2): s1, s2 = s2, s1
            for w1 in s1: # level order
                new_words = [w1[:i] + t + w1[i+1:]  for t in string.ascii_lowercase for i in range(l)]
                for w in new_words:
                    if w in s2: return level + 1
                    if w not in wordList: continue
                    s.add(w)
                    wordList.remove(w)
            s1 = s
        return 0
    