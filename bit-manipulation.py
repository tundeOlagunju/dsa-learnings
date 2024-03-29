import math
#xor is its own inverse e.g
# (x ^ y)^ y ==> x because y ^ y = 0 and x ^ 0 = x

#Python does not store -ve numbers in twos complement. instead it uses signs e.g
# print(bin(-42))

#To force python to store as 2s complement we use a mask 
mask = 255 #this mask also ensures a number is in 8 bits
# print(bin (-42 & mask))

#bitwise NOT always produces negative number when applied on a +ve number
# print (~156) #should return 99 but instead returns -157
# print (~156 & mask) #returns 99. the mask forces the number to use 2s complement
# print(-157 & mask) #returns 99

# Bitwise ANDing in order to extract a subset of the bits in the value
# Bitwise ORing in order to set a subset of the bits in the value
# Bitwise XORing in order to toggle a subset of the bits in the value

# & 1 => is kind of soft, it just tells us if the bit is set or not 
# | 1 => is not soft, mutates the bit for that position to 1
# ^ 1 => returns the opposite of the bit at a position

# & 0 => not soft, mutates the bit to 0
# ^ 0 => soft, returns the bit at the position


#basically checking if the last bit is not set i.e 0
def is_even(num):
    num & 1 == 0 # why? e.g 126 == 11111110 & 00000001  == 0. last bit of an even number is always 0; 0 and 1 is 0

#basically checking if the last bit is set i.e 1
def is_odd(num):
    num & 1 == 1 # last bit of an odd number is 1. 1 & 1 == 1. 23 == 10111 & 00001 = 1

#basically checking if the bit at a particular index is set. Zero based index (from the back)
def is_bit_set(value, index):
    return (value >> index) & 1 == 1 #shifting all the bits infront of the interested index to the right. This shifting makes the interested 
    #bit to be the last bit/lsb. We then check if the last bit is set just like above
print(is_bit_set(0b01001,12))

# same as above but getting the bit
def get_bit(value, index):
    return (value >> index) & 1

# print(get_bit(32, 5))
# print(get_bit(0b100000, 5))

def get_bit_2(value, index):
    return value & (1 << index) # 0 if the bit is not set 2^index if set. In this approach, rather than shifting the value itself, we shift 
    #1 to match the index in the value e.g get_bit_2(101000 , 2) ==> we left shift 1 twice i.e 1 << 2 to give 100. At this point 1 is at index 2(from the back)
    # we then evaluate 101000 & 000100 = 0 which means the bit is not set, if it was 1 we get 100 as result which is 2^index (2^2)

# print(get_bit_2(32, 5))
# print(get_bit_2(0b100000, 5))

#sets bit at a particular index to 1 if it was 0
def set_bit(value, index):
    return value | (1 << index)

print(bin(set_bit(0b100010, 1)))
print(bin(set_bit(54, 2)))

def clear_bit(value, index):
    return value & ~(1 << index) # (11111000,2). ~(1 << 2) returns 011. which ensures we apply &0 at the interested index. &0 mutates the bit to 0
    #having 1s at other places ensure we copy over the bits

# print(bin(clear_bit(0b1111100, 2)))


def toggle_bit(value, index):
    return value ^ (1 << index) #A binary one on the specified position will make the bit at that index invert its value. 
    #Having binary zeros on the remaining places will ensure that the rest of the bits will be copied

#https://betterexplained.com/articles/swap-two-variables-using-xor/
#dontrythisathome
def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y


def majority_element(nums):
    bits = [0]*32
    for index in range(len(bits)):
        for num in nums:  
            if is_bit_set(num, index):
                bits[31-index] += 1

    ret = ['1' if bit > len(nums)//2 else '0' for bit in bits]  
    return int(''.join(ret), 2)
   
print(majority_element([2,3,4,2,2]))

# a << n = a * 2^N
#convert binary to decimal
def convert(binary):
    ret = 0
    for i in range(len(binary)):
        # ret += binary[i] * 2**(len(binary)-1-i)
        ret += binary[i] << (len(binary)-1-i)
    return ret

# print(convert([1,1,1]))

# https://stackoverflow.com/questions/4678333/n-n-1-what-does-this-expression-do
def isPowerOf2(num):
    return num > 0 and num & (num- 1) == 0



# for any number n, doing a bit-wise AND of n and n - 1flips the least-significant 1-bit in n to 0

# n & n-1 filps the last set bit alone

# How to get / isolate the rightmost 1-bit : x & (-x).

# How to turn off (= set to 0) the rightmost 1-bit : x & (x - 1).

# The idea behind both solutions will be the same: a power of two in binary representation is one 1-bit, followed by some zeros:

# 1 = (00000001) 
# 2 = (00000010) 
# 4 = (00000100) 
# 8 = (00001000) 



#count 1s in bits
def pop_count(x: int):
    count = 0
    while x != 0:
        x &= x - 1 # zeroing out the least significant nonzero bit
        count += 1
    return count  

print(pop_count(3))

# think about the number of bits in 2**3 to 2**4 - 1 (they are all 4 bits) therefore log(2)n + 1 will give number of bits for that number
# https://www.exploringbinary.com/number-of-bits-in-a-decimal-integer/
def countBits(number): 
    # log function in base 2
    # take only integer part
    # log(2)x = log(10)2 / log(10)x
    
    return int((math.log(number) /
                math.log(2)) + 1)


 # This is magic lool but it makes sense!!
# https://leetcode.com/problems/sum-of-two-integers/


#  XOR is a difference of two integers without taking borrow into account.
# XOR is a key as well because it's a sum of two integers in the binary form without taking carry into account

# Simulate borrow this way
# Took me a while to understand why borrow = (~x & y) << 1 in Approach 1. Well, simply put, for each position where a bit of x is zero (~x) 
# and (&) a bit of y is one (y), you have to borrow a 1 one position left of that position (<< 1).


# Simulate carry this way
# For everywhere x is 1  and (&) y is 1, carry 1 to the left << . i.e (x & y << 1)



# Took me a while to understand why borrow = (~x & y) << 1 in Approach 1. Well, simply put, for each position where a bit of x is zero (~x) 
# and (&) a bit of y is one (y), you have to borrow a 1 one position left of that position (<< 1).



print((1 << 128) >> 128 & 1)


#https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/



mask2 = 0xFFFFFFFF
print(bin (-6 & mask2))
# print(bin (-42))
# print(bin (42) + bin(1))

# print(int("10101", 2)) #
print(int("0xFFFFFFE2", 16))
print(hex(4294967266))

# print(len("11111111111111111111111111111100"))

num = -20
unsigned = num if num >= 0 else (1 << 32) + num #signed to unsigned
print(format(unsigned, '032b'))
print(bin(unsigned))

# print(format(-6, '05b'))

# print(bin(-20))
# print(int("11100", 2))

#https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

#https://stackoverflow.com/questions/7822956/how-to-convert-negative-integer-value-to-hex-in-python
#https://stackoverflow.com/questions/20766813/how-to-convert-signed-to-unsigned-integer-in-python
#https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
#https://en.wikipedia.org/wiki/Two%27s_complement
def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))
  #return hex((val + (1 <<  32)) % (1 << 32)) using hex() adds Ox to the front of the result
  #return format((val + (1 <<  32)) % (1 << 32), 'x') gives the result without Ox

#OR

def toHex(self, val):
    if val < 0:
        return format((val + (1 <<  32)), 'x') #signed to 32 bit unsigned if -ve (32 bit is integer)
    else: return format(val, 'x')