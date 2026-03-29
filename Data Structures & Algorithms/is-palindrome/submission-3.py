class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char for char in s if char.isalnum())
        j = len(string) - 1
        for i in range(0,len(string)):
            if(string[i].lower() != string[j].lower()):
                return False
            j -= 1
        return True