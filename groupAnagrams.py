'''
idea_0: create key out of each set of letters and use it as a way to group anagrams in hashtable
O(n * word_length), O(n * word_length) or O(n) if excluding answers

def groupAnagrams(strs):
    groups = dict()
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return [groups[k] for k in groups]
'''

'''
idea_1: sort all by word length, then by anagram square val
    - wont word, think about ladder leaning on wall and slipping down
'''

'''
idea_2: sort all by word length, then sort by a string formed by the coutns of letters at each index

def groupAnagrams(strs):
    letter groups = dict
    for each word in strs
        # get the letterCounts string
        letter counts = [0,0,0...0,0]
        for letter in word
            increment the index of the value of the letter in letterCounts
        turn letter coutns into string
        
        if letterCounts is in groups
            find bucket by key and append to array
        else if not in group 
            create new group with array(word)
    turn dict into list and return
'''
def groupAnagrams(strs):
    groups = dict()
    for word in strs:
        letterCounts = [0 for i in range(26)]
        for letter in word:
            letterCountIdx = ord(letter) - ord('a') 
            letterCounts[letterCountIdx] += 1
        key = ','.join([str(count) for count in letterCounts])
        
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return [groups[k] for k in groups]

strs = ["bdddddddddd","bbbbbbbbbbc"]
ans = groupAnagrams(strs)
print(ans)

