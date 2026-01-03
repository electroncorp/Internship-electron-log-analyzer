def is_palindrome(s):
    s = s.lower()
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch

    rev = ""
    pos = len(cleaned) - 1
    while pos >= 0:
        rev += cleaned[pos]
        pos -= 1

    return cleaned == rev

print(is_palindrome("racecar"))
print(is_palindrome("RaceCar"))
print(is_palindrome("Hello"))
print(is_palindrome(""))
print(is_palindrome("12321"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No 'x' in Nixon"))
print(is_palindrome("abc123"))
