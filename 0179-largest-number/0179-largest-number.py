class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        current_max,answer="",""
        
        nums=[str(num) for num in nums]
        while nums:
            for num in nums:
                if not current_max:
                    current_max=num
                else:
                    if num+current_max>current_max+num:
                        current_max=num
            answer+=current_max
            nums.remove(current_max)
            current_max=""
        return answer if not answer.startswith("0") else "0"
        