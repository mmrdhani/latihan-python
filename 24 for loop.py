#akan belajar tentang for looping 
#looping ini selama angak yang berada salam range atau list masih ada, maka akan looping
print("LOOPING DENGAN LIST".center(38,"="))
list_angka = [0,1,2,3,4,5]

for i in list_angka:
    print(f'angka sekarang {i}')
print('akhir dari program 1\n')

print("LOOPING DENGAN RANGE".center(38,"="))
range_angka = range(0,5) #harus ada operator range-nya
for i in range_angka:
    print(f'angka sekarang {i}')
print('akhir dari program 2\n')

print("LOOPING HURUF".center(38,"-"))
data_str = "aku keren abiss"
for huruf in data_str:
    print(huruf)
print("akhir dari program 3")