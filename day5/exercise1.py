def check(text):
    if text == text[::-1]:
        print(f"{text} is palindrome word")
    else:
        print(f"{text} is not palindrome word")
        
user = input('Masukkan Kata : ')
check(user)