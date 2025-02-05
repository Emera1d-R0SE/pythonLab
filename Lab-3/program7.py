#palindrome even for first letter caps. 
def is_palindrome(string):
    left, right =0, len(string) -1
    string2=string.upper()
    while right>=left:
        if string2[left]!=string2[right]:
            return False
        left+=1
        right-=1
    return True
print(is_palindrome('Racecar'))
