from collections import deque

def is_palindrome(input_string:str):
    normalized_str = input_string.lower()
    normalized_str = normalized_str.replace(' ','')
    
    char_deque = deque(normalized_str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True