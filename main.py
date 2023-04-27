#2
s = input('Введіть рядок: ')
def palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(palindrome(s))