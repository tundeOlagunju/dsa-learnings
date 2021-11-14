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
print(is_bit_set(0b01001,0))

# same as above but getting the bit
def get_bit(value, index):
    return (value >> index) & 1

# print(get_bit(32, 5))
# print(get_bit(0b100000, 5))

def get_bit_2(value, index):
    return value & (1 << index) # 0 if the bit is not set 2^index if set. In this approach, rather than shifting the value itself, we shift 
    #1 to match the index in the value e.g get_bit_2(101000 , 2) ==> we left shift 1 twice i.e 1 << 2 to give 100. At this point 1 is at index 2.
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
   
# print(majority_element([2,3,4,2,2]))

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

