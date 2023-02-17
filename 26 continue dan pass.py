#akan belajar continue, pass, dan break
#pass akan berfungsi sebaagai dummy, atau tidak akan dieksekusi

angka = 0
while angka <10:
    angka += 1
    if angka ==3:
        pass #akan dilewati, atau tidak dieksekusi
    else:
        print('bukan angka 3')
    print(f'angka sekarang adalah {angka}')
print('akhir dari program\n\n')

#continue
angka = 0
while angka <5:
    angka += 1
    print(f'angka sekarang {angka}')
    if angka == 3:
        print('sebelum continue')
        continue
        print('setelah continue') #ketika kontinu program akan dilewati
    else:
        print(f'angka selain tiga{angka}') #ketika kontinu program akan dilewati
    print(f'hai!') #ketika kontinu program akan dilewati, balik lagi ke loop awal
print('akhir dari program continue')

