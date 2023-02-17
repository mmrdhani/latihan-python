#operasi pada string ini sangata banyak
#kali ini akan dibahas mengenai
#1. menyambung string, 2. menghitung panjang string, 
#3. oprator untuk string, dan 4. operatr dalam bentuk method

print(10*'=','MENYAMBUNG STRING',10*'=')
nama_depan    = "ucup"
nama_tengah   = "binu'"
nama_belakang = "Fritz"
nama_lengkap  = nama_depan + " " + nama_tengah + " " + nama_belakang
#cara menyambungkan data string adalah dengan tambah
print('Nama lengkapnya adalah: ', nama_lengkap)
#pada print(), menyambungkan data string boleh menggunakan tanda + atau tanda ,
print('\n'+ 8*'=','MENGHITUNG PANJANG STRING',8*'=')
panjang = len(nama_lengkap)
print('panjang dari:', nama_lengkap , ' adalah:' , str(panjang))
#panjang harus di casting agar menjadi data str

print('\n','MENGECEK ADAKAH KOMPONEN CHAR ATAU STRING DI STRING')
d ="d"
status = d in nama_lengkap
print("ada komponen: ", d, 'di', nama_lengkap, "adalah", status)

f ="F"
status = f in nama_lengkap
print("ada komponen: ", f, 'di', nama_lengkap, "adalah", status)
f ="f"
status = f not in nama_lengkap
print("ada komponen: ", f, 'di', nama_lengkap, "adalah", status)

print(10*'=',10*'MENGULANG STRING',10*'=')

#indekxing
print('\n____indeks____')
#indexing untuk mengambil karakter dari sebuah string
#karakter yg diambil terserah, urutan, loncat, atau satu deret
print("indek ke [0] dari "+ nama_lengkap + ' = ' + nama_lengkap[0])
print("indek ke [1] dari "+ nama_lengkap + ' = ' + nama_lengkap[1])
print("indek ke [2] dari "+ nama_lengkap + ' = ' + nama_lengkap[2])
print("indek ke [3] dari "+ nama_lengkap + ' = ' + nama_lengkap[3])
print("indek ke [4] dari "+ nama_lengkap + ' = ' + nama_lengkap[4])
print("indek ke [5] dari "+ nama_lengkap + ' = ' + nama_lengkap[5])
print("indek ke [6] dari "+ nama_lengkap + ' = ' + nama_lengkap[6])
print("indek ke [7] dari "+ nama_lengkap + ' = ' + nama_lengkap[7])
print("indek ke [8] dari "+ nama_lengkap + ' = ' + nama_lengkap[8])
print("indek ke [9] dari "+ nama_lengkap + ' = ' + nama_lengkap[9])
print("indek ke [10] dari "+ nama_lengkap + ' = ' + nama_lengkap[10])
print("indek ke [11] dari "+ nama_lengkap + ' = ' + nama_lengkap[11])
print("indek ke [12] dari "+ nama_lengkap + ' = ' + nama_lengkap[12])
print("indek ke [13] dari "+ nama_lengkap + ' = ' + nama_lengkap[13])
print("indek ke [14] dari "+ nama_lengkap + ' = ' + nama_lengkap[14])
print("indek ke [15] dari "+ nama_lengkap + ' = ' + nama_lengkap[15])
"""jika indeksnya negatif, maka akan diambilkan dari belakang
namun, jika indeks yang diminta lebih dari panjang string, maka akan error"""
print('\n____indeks negatif____')
print("indek ke [-1] dari"+ nama_lengkap + ' = ' + nama_lengkap[-1])
print("indek ke [-4] dari"+ nama_lengkap + ' = ' + nama_lengkap[-4])
print('\n____indeks dalam retang____')
print("indek ke [0:3] dari"+ nama_lengkap + ' = ' + nama_lengkap[0:4])
#khusus pd rentang, index yg diminta harus lebih dari 1, sehingga [0,(3+1)]
print("indek ke [2:15:2] dari"+ nama_lengkap + ' = ' + nama_lengkap[2:15:2])

print('\n____item paling kecil/ besar____')
print('item paling kecil dari '+nama_lengkap+' '+ min(nama_lengkap))
print('item paling besar dari '+nama_lengkap+' '+ max(nama_lengkap))

print('\n____operator dalam bentuk method____')
nama = "Muhammad Ahmad bin Muhammad al Ramdhani"
#operator ini untuk mengetahui banyaknya dari sebuah karakter di dalam data string
jumlah = nama.count('m')
print('banyaknya m pada'+ nama+ ': '+ str(jumlah))

"""tipe data string ini akan sangat penting untuk dipelajari untuk program-program berikutnya"""