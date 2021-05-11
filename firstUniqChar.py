def firstUniqChar1(s):
    char ={}
    for x in s: # n
        if x in char:
            char[x] +=1
        else:
            char[x] =1
    # print(char)
    for x in char: #  = m 
        # print(x,char[x])
        if char[x] == 1:
            return s.index(x)  #  = n
    return -1

#O(n) = n + (n+m)  = 2n = n
    
from collections import defaultdict
def firstUniqChar2(s):
    char = defaultdict(int)
    for i in s: 
        char[i] += 1
    for i in s:
        if char[i]==1:
            return s.index(i)
    return -1


from collections import defaultdict,Counter
def firstUniqChar3(s):
    word = list(s)
    count = Counter(word)

    # print(count)
    # print(count.most_common(1))
    for i in s:
            if count[i]==1:
                return s.index(i)  
    return -1

print(firstUniqChar1('noor'))
print(firstUniqChar1('leetcode'))
print(firstUniqChar1('loveleetcode'))
print(firstUniqChar2('noor'))
print(firstUniqChar2('leetcode'))
print(firstUniqChar2('loveleetcode'))
print(firstUniqChar3('noor'))
print(firstUniqChar3('leetcode'))
print(firstUniqChar3('loveleetcode'))
