"""
DI SINI AKAN BELAJAR FORMATING
1. STRING
2. ANGKA 
3. BOOLEAN
4.BILANGAN BULAT
5.BILANGAN RIIBUAN
6.BILANGAN DESIMAL
7. LEADING ZERO
8. TANDA + ATAU -
9. FOMAT PERSEN
10. MELAKUKAN OPERASI DI PLACEHOLDER
11. FORMAT ANGKA LAIN: BINARY, HEXAL, OCTAL
"""
##STRING
nama = "ucupp"
print('nama : '+ nama)
#diatas bisa diformating dengan:
format_nama = f'nama : {nama}'
print(format_nama)

##ANGKA
angka = 2003.4321
print('angka : '+ str(angka)) #harus casting dulu
#diatas bisa diformating dengan:
format_angka = f'angka : {angka}'
print(format_angka)

##BOOLEAN
boolean = True 
print('boolean : '+ str(boolean)) #harus casting dulu
#diatas bisa diformating dengan:
format_boolean = f'boolean : {boolean}'
print(format_boolean)

##BILANGAN BULAT
bilangan_bulat = 17
print('bilangan bulat : '+ str(bilangan_bulat)) #harus casting dulu
#diatas bisa diformating dengan:
format_bilangan_bulat = f'bilangan bulat : {bilangan_bulat:d}' 
#jika diformat f'bilangan bulat : {bilangan_bulat:d}' tanda d disitu berarti
#berarti untuk mengecek data yang diformat itu harus bertipe integer
#jika bukan integer, maka akan error
print(format_bilangan_bulat)

##RIBUAN
ribuan = 35400000 
format_ribuan = f'ribuan : {ribuan:,}' #tanda koma berarti pemisah ribuan
print(format_ribuan)

##DESIMAL
desimal = 356.783201 
format_desimal = f'desimal : {desimal:.4f}' #tanda titik diambil dari pemisah desimal
#angka 2 berarti banyaknya digit yang akan diambil
#jika banyakkny digit yg diminta lebih besar dari yg tersedia, maka akan ditambahkan 0
#huruf f berati dari data float-nya
print(format_desimal)

##LEADING ZERO
angka = 3462.123456 
format_angka = f'leading zero : {angka:9.3f}' 
#angka didpean koma berarti banyaknya karakter yg akan diambil
#angka ini minimal adlh banyakny karakter didepan titik, titiknya, dan dari "3f"
#jika lebih kecil, maka tidak bisa, jika lebih besar akan diisi space di depan bilangan
#3f sama seperti aturan untuk banyaknya desimal yang akan diambil
print(format_angka)
format_angka = f'leading zero : {angka:8.3f}' 
print(format_angka)
format_angka = f'leading zero : {angka:014.4f}' #jika ditambah 0, maka a
print(format_angka)

##TANDA + DAN -
angka_min = -34
angka_plus = 34
angka_plusdeci = 34.544324
format_min = f"format angka: {angka_min:+d}"
format_plus = f"format angka: {angka_plus:+d}"
format_angka_plusdeci = f' format angka desimal: {angka_plusdeci:+.3f}'
#juga dpt dikerjakan pd angka desimal yg positif, dan ditentukan banyaknya digit dibelaakang titik
print(format_min)
print(format_plus)
print(format_angka_plusdeci)

##PERSEN
angka = 0.032
persentase = f'persentase : {angka:%}' #tinggal atambahkan persen
print(persentase)
persentase = f'persentase : {angka:.2%}' 
#digit dibelakang titik juga dapat diatur dengan angka di depan karakter %
print(persentase)
persentase = f'persentase : {angka:+.3%}' #boleh dikasih tanda positif
print(persentase)
print(type(persentase)) #tipe dari ini adalah string
##OPERSAI DI PLACEHOLDER
#melakukan operasi aritmatika di placeholder
panjang = 13
lebar = 4
tinggi = 6
luas_permukaan =f"luas permukaan balok: {2*(panjang*lebar+panjang*tinggi+tinggi*lebar)} cm^2"
print(luas_permukaan)
#juga bisa diatur desimal, positif. negatifnya, dll

##FORMAT BILANGAN LAIN: BINER, HEXAL, OCTAL
angka = 200
formaat_binary = f'format biner: {bin(angka)}'
format_hex = f'format hexal: {hex(angka)}'
format_oct = f"format octal: {oct(angka)}"
print(formaat_binary)
print(format_hex)
print(format_oct)
