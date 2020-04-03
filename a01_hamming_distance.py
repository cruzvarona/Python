#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
#Given two integers x and y, calculate the Hamming distance.
#
#Note:
#0 ≤ x, y < 231.
#
#Example:
#
#Input: x = 1, y = 4
#
#Output: 2
#
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#          ↑   ↑
#
#The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        x_bits = "{0:b}".format(x)
        y_bits = "{0:b}".format(y)
        
        # iterate from the right side of both the longer/or one equally long string
        if len(x_bits) > len(y_bits):
            longer = x_bits
            shorter = y_bits
        else:
            longer = y_bits
            shorter = x_bits
        
        for idx in range(0,len(longer),1):
            if idx < len(shorter):
                if longer[len(longer)-idx-1] != shorter[len(shorter)-idx-1]:
                    distance+=1
            else:
                if longer[len(longer)-idx-1] == "1":
                    distance+=1
            
            print("idx = {}, distance = {}".format(idx,distance))
    
        return distance


