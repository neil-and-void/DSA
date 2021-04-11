'''
def toHex(num):
    s = Stack()

    while num > 0:
        digit = num mod 16
        num = num // 16 # shifts to the right to put into position to get the next digit


'''


def toHex(num):
    hexDigits = '0123456789abcdef'
    stack = []

    if num < 0:
        # get 32 bit 2's complement representation of the number if negative
        num = 0xffffffff + 1 + num
    while num > 0:
        digit = num % 16
        num //= 16
        stack.append(digit)

    ans = ''

    while len(stack):
        ans += hexDigits[stack.pop()]
    return ans














'''
def toBase(base, num):
    baseDigits = '01234567890abcdef'

    base case
    if the num < base:
        return baseDigts[num]

    recursiev case
    digit = modulo the number in base
    num = num // base # shifts the num over by 1 base
    return toBase(base, num).concat(baseDigits[digit])
'''

# convert to any base max 16
def toBase(base, num):
    baseDigits = '0123456789abcdef'

    # base case
    if num < base:
        return baseDigits[num]

    # recursive case
    digit = num % base
    num = num // base
    return toBase(base, num) + baseDigits[digit]

def main():
    # num = -1
    # result = toHex(num)
    # print(result)
    num = 23467
    result = toBase(16, num)
    print(result)

if __name__ == '__main__':
    main()

