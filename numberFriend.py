def numberFriend(group):
    friendTable = dict()
    for i in range(len(group)):
        print(friendTable)
        friend = (group[i] * 3) - 2
        friendComplement = (group[i] + 2) / 3
        if friend in friendTable:
            return [i, friendTable[friend]]
        if friendComplement in friendTable:
            return [i, friendTable[friendComplement]]
        friendTable[friend] = i
        friendTable[friendComplement] = i





g = [2, 8, 5, 4 ,6, 10]
ans = numberFriend(g)
print(ans)

