#disini akan belajar tentang logika dan komparasi
#yaitu dengan materi himpunan
print("\n", "===PROGRAM LOGIKA DAN KOMPARASI===\n")
#akan dibuat daerah himpunan yang memenuhi
# dimana {x<0 dan 5<x<8 dan x>11}
print("Akan dicek apakah nilai x yang dimasukkan \n kurang dari 3 atau diantara 5 dan 8 atau lebih dari 11")
x = float(input("masukkan nilai x: "))

isx1 =(x<3)
isx2 = (x>5)
isx3 = (x<8)
isx4 = (x>11)

xHasil= (isx1) or (isx2 and isx3) or isx4
print("Hasil yang diimput adalah", xHasil)

print('\n ===KOMPARASI LAIN===', 3*'\n')
#daerah yang memenuhi {y<=5 dan 10<y<=14}
y = float(input('Masukkan y dengan y<=5 atau 10<y<=14: '))
isy1 = (y<=5)
isy2 = (y>10)
isy3 = (y<=14)

yAkhir = isy1 or (isy2 and isy3)
print('Bilangan yang anda masukkan adalah: ', yAkhir)

