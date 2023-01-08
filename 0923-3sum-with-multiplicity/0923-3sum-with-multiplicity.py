class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dic={}
        
        mod=1e9 +7
        result=0
        
        for ele in arr:
            dic[ele]=1 + dic.get(ele, 0)
        
        for key1 in dic:
            for key2 in dic:
                key3= target - key1 - key2
                if key3 not in dic: 
                    continue
                if key1==key2 and key2== key3:
                    result+= ((dic[key1] * (dic[key1] -1) * (dic[key1] -2))//6 )
                elif key1==key2 and key2 != key3:
                    result+=((dic[key1] * (dic[key1] -1) * dic[key3])//2)
                elif key1 < key2 and key2 < key3:
                    result += (dic[key1] * dic[key2] * dic[key3])
        return int(result % mod)
                
                
        