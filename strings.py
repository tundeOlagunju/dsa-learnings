import functools, string
def isUnique(string):
    # Assume ASCII - 128
    if len(string) > 128:
        return False
    char_set = [False] * 128
    for ch in string:
        if char_set[ord(ch)]:
            return False
        char_set[ord(ch)] = True
    return True

def isUniqueBitMan(string):
    checker = 0
    for ch in string:
        # is bit set
        # return (value >> index) & 1 == 1 
        if checker & (1 << ord(ch) - ord('a')) > 0:
            return False
        # set bit
        checker = checker | 1 << ord(ch) - ord('a')
    return True

# print(isUnique('abd'))
# print(isUniqueBitMan('abd'))

def isPermutationOfOther(string1, string2):
    # if 2 strings are permutation of each other, they must have identical character counts
    if len(string1) != len(string2):
        return False

    freq_set = [0] * 128
    for ch in string1:
        freq_set[ord(ch)] += 1
    
    for ch in string2:
        freq_set[ord(ch)] -= 1
        if freq_set[ord(ch)] < 0:
            return False
    return True

# print(isPermutationOfOther('abbd', 'badc'))

def ispalindromic (s) :
# Note that s[-jJ for i in [0,len(s) - 1] is st-(i + t)l
    return all(s[~i] == s[-i] for i in range(len(s) // 2))

def convertStrToInt(string1):
    res = 0
    for i in range(len(string1)):
        power = len(string1) - i - 1
        res += (ord(string1[i]) - ord('0')) * (10 ** power)
    return res

def convertStrToInt2(string1):
    res = 0
    for i in range(len(string1)):
        # print(string.digits.index(string1[i]))
        # res = (ord(string1[i]) - ord('0')) + res * 10 
        res = string.digits.index(string1[i]) + res * 10 
    return res

print(convertStrToInt2("123"))

def convertIntToStr(integer):
    res =  []
    while integer > 0:
        last = integer % 10
        res.append(chr(ord('0') + last))
        # res.append(str(last))
        integer //= 10

    return "".join(reversed(res))
    # return "".join(res[::-1])

# print(convertIntToStr(123))


def stringToIntFunctional(s) :
    # print(s[True:])
    # print( s[ s[0] == '-': ] )
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c) , s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

print(stringToIntFunctional('615'))

# is_negative = '-' == '-'
# print(('-' if is_negative else ""))

print(string.hexdigits[306%13])
print(string.digits.index('1'))
print(string.digits[ord('1') - ord('0')])

def spreadSheetEncoding(column_id):
    res = 0
    for i in range(len(column_id)):
        # res += ord(column_id[i]) - ord('A') + 1 * (26 ** i)
        res = res * 26 + ord(column_id[i]) - ord('A') + 1
    return res

def spreadSheetEncodingFunctional(column_id):
    return functools.reduce( lambda result, c: result * 26 + ord(c) - ord('A') + 1, column_id, 0)





print(spreadSheetEncoding("B"))

print("hello"[4:909])