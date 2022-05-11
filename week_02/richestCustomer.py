# You are given an m x n integer grid accounts 
# where accounts[i][j] is the amount of money the 
# i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth 
# that the richest customer has.

# A customer's wealth is the amount of
#  money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        re=[]
        for lst in accounts:
            sum=0
            for i in range(len(lst)):
                sum+=lst[i]
                re.append(sum)
        largest=re[0]
        for j in range(len(re)):
            if re[j]>largest:
                largest=re[j]
        return largest