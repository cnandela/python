def is_palindrame(s):
    s = s.lower()
    s = s.replace(" ","")
    return s == s[::-1]

print(is_palindrame("madam"))
