
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char ={}
        for x in s: # n
            if x in char:
                char[x] +=1
            else:
                char[x] =1
        print(char)
        for x in char: #  = m 
            print(x,char[x])
            if char[x] == 1:
                return s.index(x)  #  = n
        return -1
    
    #O(n) = n + (n+m)  = 2n = n
        
class Solution:
    from collections import defaultdict
    def firstUniqChar(self, s: str) -> int:
        char = defaultdict(int)
        for i in s: 
            char[i] += 1
        for i in s:
            if char[i]==1:
                return s.index(i)
        return -1

    
class Solution:
    from collections import defaultdict
    def firstUniqChar(self, s: str) -> int:
        word = list(s)
        count = Counter(word)
    
        print(count)
        print(count.most_common(1))
        for i in s:
                if count[i]==1:
                    return s.index(i)  
        return -1
