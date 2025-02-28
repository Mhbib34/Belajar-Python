import exercise3 as exe

def check():
    user = input('Masukkan Kata : ')
    result = exe.count_vowels_and_check_palindrome(user)
    print(f"Jumlah huruf vokal: {result['vowel_count']}")
    print(f"Apakah palindrome: {'Ya' if result['is_palindrome'] else 'Tidak'} \n")

while True:
    print('MENU')
    print('1.Cek jumlah vokal dan palindrome')
    print('2.Balikkan kata')
    print('3.Exit')
    user = int(input('Pilih [1,2,3] '))
    
    if user == 1:
        check()
    elif user == 2:
        input_user = input('Masukkan kata : ')
        print(f'Hasilnya adalah : {exe.reverse(input_user)}\n')
    elif user == 3:
        print('Exiting Program')
        break
    else:
        print('Anda salah memasukkan angka!')
        break