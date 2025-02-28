def reverse(nama):
     return nama [::-1]
 
def count_vowels_and_check_palindrome(input_string):
    input_string = input_string.lower()

    vowels = {'a', 'i', 'u', 'e', 'o'}

    vowel_count = sum(1 for char in input_string if char in vowels)

    is_palindrome = input_string == input_string[::-1]

    return {
        'vowel_count': vowel_count,
        'is_palindrome': is_palindrome
    }
