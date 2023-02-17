print("Program Nilai Ulangan".center(20,"=")+2*"\n")
nilai = int(input("Masukkan nilai ulangan: "))
#harus dicasting karena typer yang diimputkan adalh bertipe string

if nilai >= 80: #if ini menggunakan type boolean, jadi menggunakan komparasi
    print("Selamat! Kamu lulus.")
else:
    print('Kamu belum lulus, belajar lagi ya!')
print("akhir dari program")
 
