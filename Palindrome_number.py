class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convert the integer to string str(x)
        #This allows us to easily compare characters
        #Reverse the string using slicing
        #Compare original and reversed string
        return str(x) == str(x)[::-1]
