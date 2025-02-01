# Python program to find length of the 
# longest valid substring 

def maxLength(s):
    max_len = 0
    
    # Left to Right Traversal
    open = close = 0
    for ch in s:
        if ch == '(':
            open += 1
        elif ch == ')':
            close += 1
        
        if open == close:
            max_len = max(max_len, 2 * close)
        elif close > open:
            open = close = 0
    
    # Right to Left Traversal
    open = close = 0
    for ch in reversed(s):
        if ch == '(':
            open += 1
        elif ch == ')':
            close += 1
        
        if open == close:
            max_len = max(max_len, 2 * open)
        elif open > close:
            open = close = 0
    
    return max_len

if __name__ == "__main__":
    s = "())"
    print(maxLength(s))