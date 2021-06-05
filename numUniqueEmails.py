'''
idea: create key out of the 'true' email of each email and add this key to a set to get num of distinct emails
'''
def numUniqueEmails(emails):
    trueEmails = set()
    for email in emails:
        trueEmail = []

        i = 0
        while email[i] != '+' and email[i] != '@':
            if email[i] != '.':
                trueEmail.append(email[i])
            i += 1

        while email[i] != '@':
            i += 1

        while i < len(email):
            trueEmail.append(email[i])
            i+=1  

        trueEmails.add(''.join(trueEmail))
        
    return len(trueEmails)

emails =  ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
ans = numUniqueEmails(emails)
print(ans)

