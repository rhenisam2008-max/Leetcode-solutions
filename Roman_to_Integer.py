class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Create a dictionary to store Roman values
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        # Step 2: Initialize total value
        t= 0
        # Step 3: Iterate through the string
        for i in range(len(s)):
            # Step 4: Check if current value is less than next value
            # This handles cases like IV (4), IX (9), etc.
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                # If smaller before larger → subtract
                t-= roman[s[i]]
            else:
                # Otherwise → add
                t+= roman[s[i]]
        # Step 5: Return final result
        return t
