print("PROGRAM NILAI ULANGAN 2.0".center(39,"="), "\n")
nilai = int(input("Masukkan nilai ulangan kamu: "))
if nilai > 80:
    print("kamu lulus.")
elif nilai == 80:
    print("kamu aman!")
elif nilai >= 60:
    print("kamu perlu remidial")
elif nilai >=0:
    print("kamu ngga naik kelas!")
else:
    print("data yang kamu masukkan salah")
print("akhir dari program")