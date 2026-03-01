class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
      
        sign = 1 if num > 0 else -1
        digits = list(str(abs(num)))  

        if sign == 1:
           
            digits.sort()                   
            
          
            i = 0
            while i < len(digits) and digits[i] == '0':
                i += 1
                
          
            result = digits[i] + ''.join(digits[:i]) + ''.join(digits[i+1:])
            return int(result)
        
        else:
          
            digits.sort(reverse=True)          
            return sign * int(''.join(digits))