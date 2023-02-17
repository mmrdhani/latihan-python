#akan belajar mengenai break
#break ini tidak akan memproses semua program yang ada dibawahnnya

a = 0
while a < 5:
    a += 1
    print(f'angka sekarang adalah {a}')
    if a ==3:
        print('nice!')
        break #break akan melompati semua yang berada dalam loop
    else:
        print("ketika angka tidak sama dengan 3")
    print('ketika program if selesai')
print('akhir daari program break')

data = input('masukkan data ')
print(f"data yang anda masukkan adalah {data}")

while a < 5:
    a += 1
    print(f'angka sekarang adalah {a}')
    if a ==3:
        print('nice!')
        
    else:
        print("ketika angka tidak sama dengan 3")
    print('ketika program if selesai')
print('akhir daari program break')