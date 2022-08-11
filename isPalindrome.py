import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ Sol 1:
                if(x < 0):
                    return False
                elif(x == 0):
                    return True

                digits = int(math.log10(x))

                firstDigit = x // 10**digits % 10
                lastDigit = x % 10; 

                counter = 1

                positionCounter = digits

                while(firstDigit == lastDigit and positionCounter >= 0):
                    firstDigit = x // 10**(digits-counter) % 10
                    lastDigit = x // 10**(counter) % 10
                    
                    counter += 1
                    
                    positionCounter -= 1

                if(positionCounter == -1):
                    return True
                else:
                    return False
        """
        if(x < 0) or (x % 10 == 0 and x != 0):
            return False
        elif(x == 0):
            return True

        reversedNumber = 0;

        while(x > reversedNumber):
            reversedNumber = reversedNumber*10 + x % 10
            x = x // 10

        return reversedNumber == x or reversedNumber // 10 == x



sol = Solution()
isPalindrome = sol.isPalindrome(10)

print(isPalindrome)