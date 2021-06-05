'''
idea: dfs/backtracking
- treat each digit as a level in the recursion tree with 3 (or 4 with) children
- dfs through each char of each number
def letterCombinations(digits):
    ans = []
    def rec(digits, candidatePath, digitIdx)
        # base
        if candidatePath length same as sdigit length (|| index == n)
            add candidatePath to answers
            return

        #recursive
        else:
            for i from 0 to dialpadDigitletters.length - 1
                append letter to candidate path
                recurse(digits, candidatePath, i+1)
                poplast letter from candidate path
'''
a = []

def letterCombinations(digits):
    def letterCombinationsRec(digits, candidatePath, digitIdx):
        # base
        if len(candidatePath) == len(digits):
            newAns = ''.join(candidatePath)
            ans.append(newAns)

        #recursive
        else:
            digit = int(digits[digitIdx])
            letters = dialpadLetters[digit]
            for letter in letters:
                candidatePath.append(letter)
                letterCombinationsRec(digits, candidatePath, digitIdx+1)
                candidatePath.pop()

    dialpadLetters = {
        2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz',
    }
    ans = []
    candidatePath = []
    digitIdx = 0
    letterCombinationsRec(digits, candidatePath, digitIdx)
    return ans

d = '23'
ans = letterCombinations(d)
print(ans)

