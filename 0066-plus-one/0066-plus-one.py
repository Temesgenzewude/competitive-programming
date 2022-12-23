class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_num=0
        dig_len= len(digits)
        for i in range(dig_len):

            int_num+= digits[i] * (10 ** (dig_len- i -1))
       
        int_num_plus_one= int_num + 1

        result= [int(x) for x in str(int_num_plus_one)]

        return result

            


        