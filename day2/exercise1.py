num = int(input('Masukkan angka : '))

if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(f'{num} is not prime number')
            break
    else:
        print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')
    