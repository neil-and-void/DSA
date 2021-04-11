'''
def reverseBits(number, hashtable):
    # idea: divide and conquer
    if num in hashtable:
        return hashtable[num]

    # base
    if num is 0 or 1:
        return num

    # recursive
    if num > 1:
        left half = num & 0xffff0000
        left half = left half >> 16

        right half = num & 0x0000ffff

        left = reverseBits(left helf)
        right = reverseBits(rigth half)

        right = right << 16
        return {right}{left}
def reverseBits(number, bits):
    # base
    bits == 1:
        return number

    # recursive
    bits > 1:
        maskLength = bits // 2
        left mask = 0xffffffff << maskLength
        right mask = 0x00000000 >> (32 - maskLength)

        left half = reverseBits((number & leftmask) >> maskLength, masklenght)
        right half = reverseBits(number & rightmask, maskLength)

        reversed = (right half << maskLength) + leftHalf
'''

def reverseBits(number):
    return reverseBitsRec(number, 32)

def reverseBitsRec(number, bitLength):
    # base
    if bitLength == 1:
        return number

    elif bitLength > 1:
        maskLength = bitLength // 2
        leftMask = 0xffffffff << maskLength
        rightMask = 0xffffffff >> (32 - maskLength)

        leftHalf = reverseBitsRec((number & leftMask) >> maskLength, maskLength)
        rightHalf = reverseBitsRec(number & rightMask, maskLength)

        reversedBits = (rightHalf << maskLength) + leftHalf
        return reversedBits


reversedBits = reverseBits(0b00000010100101000001111010011100)
print(964176192 == reversedBits)
print('{:032b}'.format(reversedBits))

reversedBits = reverseBits(0b11111111111111111111111111111101)
print(3221225471 == reversedBits)
print('{:032b}'.format(reversedBits))
