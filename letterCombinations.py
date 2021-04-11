'''
def letterCombinations(digits):
    # base
    if there is only 1 digit:
        return each letter as its own combination

    # recursive
    else:
        permsForCurrent = []
        for each letter in current digit
            append letter to each permutation of letterCombinations(digits - 1)
            
'''

def letterCombinations(digits):
    letters = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'truv',
        9: 'wxyz'
    }

    return letterCombinationsRecursive(digits, letters, len(digits) - 1)

def letterCombinationsRecursive(digits, letters, idx):
    # base case
    if len(digits) == 1:
        return len(letters[digits])

    else:
        total = 0
        for letter in letters[digits[idx]]:
            total += letterCombinationsRecursive(digits, letters, idx - 1)
        return total

