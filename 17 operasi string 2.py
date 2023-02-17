#operasi string ini lanjutan dari operasi string pada file 16
#operator dalam bentuk method

##merubah UPPER dan lower

#ke UPPER
salam = "hai, pagi!"
print('normal: '+ salam)
salam_upper = salam.upper()
print("salam upper: " + salam_upper)

#ke lower
normal = 'Aku KereN BangetzzZ'
print('normal: '+ normal)
normal_lower = normal.lower()
print("normal lower: "+ normal_lower)
print("normal upper: "+ normal.upper())

##pengecekan UPPER dan lower dengan isX method
salam="gan!"
cek = salam.islower()
print("apakah ", salam, "lower: ", cek)
print("apakah ", salam, "upper: ", salam.isupper())

salam="halo"  #spasi tidak termasuk akrakter huruf
cek = salam.isalpha()
print("apakah ", salam, "huruf: ", cek)
print("apakah ", salam, "angka: ", salam.isdecimal())
salam="123halo"
cek = salam.isalnum()
print("apakah ", salam, "alfa numerik: ", cek)
print("apakah ", salam, "space: ", salam.isspace())
salam="\n    " #space di sini adalah spasi, tab, atau new line (\n)
print("apakah ", salam, "space: ", salam.isspace())

print("\n++++ Cek Judul ++++\n")
judul = "Evektifitas Modul Adik Pintar Pada Smp Darul Falah Ditinjau Dari Critical Thinking Siswa"
print('apakah: '+judul+" judul? "+str(judul.istitle()))
#jadi, judul dimulai dengan uppercase dan yang lainnya lower
#ngga boleh satu kata saja yg capslk

print("\n++++ Cek Starswith dan edswith ++++\n")
judul = "Boruto: Naruto Next Generation"
cek_starts=judul.startswith("Boruto")
#strartswith ini cara kerjanya, membandingakan persis, satu satu karakter dari awal
print('Judul: '+ judul+ "dimulai Boruto "+ str(cek_starts))

cek_ends = judul.endswith("Generation")
#cara kerjanya persis dengan startswith, tetapi dari belakang
print('Judul: '+ judul+ "diakhiri Generation "+ str(cek_ends))

print("\n++++ Penggabungan Pemisahan Komponen ++++\n")
pisah = ['aku','sayang','kamu']
gabung = ",,".join(pisah) #karakter yg digunakan gabung itu terserah
print('bentuk pisah:', pisah)
print("bentuk gabung: ", gabung)

gabung = " ehm ".join(pisah) #karakter yg digunakan gabung itu terserah
print('bentuk pisah:', pisah)
print("bentuk gabung: ", gabung)

dipisah = gabung.split("ehm")
print("bentuk split: ", dipisah)
#yang pemisahnya menggunakan ehm, jadi karakter spasi masih ada 

##alokasi karakter, rjust(), ljust(), center()
kanan = "kanan".rjust(15) #boleh tidak didefinisikan kanannya
print("'", kanan, "'")

kiri = "kiri" #boleh didefinisikan kirinya
kiri = kiri.ljust(15) #otomatis akan diisikan space
print("'", kiri, "'")

print("'", "center".center(15), "'") #boleh langsung
#untuk mengganti space dengan karakterlain, tingal ditambahkan indeks setelah perator center( , (indeks))
print("'", "center".center(15,"#"), "'") 

#kebalikannya
center = "center".center(15,"=")
print("\n", center, "\n")
normal = center.strip("=")
print("normalnya: \n", normal)




