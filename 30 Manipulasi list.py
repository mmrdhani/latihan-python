"""
manipulasi list itu ada banyak, diantarnya: (1) Mengambil data dari list
(2) mengambil info banyaknya datum/ jumlah daata, (3) menambahkan datum 
pada suatu posisi, (4) menabahkan datum di akhir list, (5) menggabungakan
dua buah list, (6) mengubah data, (7) meremove data
"""
#data  = ["ucup",  "otong",  "jajang"]
#indeks:  0/(-3)    1/(-2)     2/(-1)

#contoh:
data = ["Ucup", "Otong", "Odah"]
print(f'daftar nama:\n{data}')
#mengambil data dari list
data_0= data[0]
print(f'\nnama pertama dari daftar: {data_0}')
data_terakhir = data [-1]
print(f'nama terakhir dalam daftar: {data_terakhir}')

#info panjang data
#sama seperti mencari banyakknya karakter pada sebuah string
panjang = len(data)
print(f'\nbanyakknya nama dalam daftar adalah: {panjang}')

#menambahkan data pada list
data.insert(1,"Ucok")
#penulisan = data.inserrt(indeks posisi, "data yg ditambahkan")
print(f'\ndaftar nama tambahan:\n{data}')

#menambahkan data di akhir list
data.append("Topek")
print(f'\ndaftar nama baru:\n{data}')

#menggabungkan 2 list
data_baru = ["Akmal", "Haris", "Hasan"]
print(f'\ndata baru: \n{data_baru}')
data.extend(data_baru)
print(f'\ndata seletah digabungkan: \n{data}')

#mengubah data
data[4]="Tomas"
print(f'\ndata setelah diubah: \n{data}')

#meremove data
data.remove("Ucok")
print(f'\ndata setelah diremove (Ucok): \n{data}')

#removing paling belakang
data.pop()
print(f'\ndata setelah diremove paling belakang: \n{data}')

#mengecek data yang diremove paling 
paling_belakang= data.pop()
print(f'\ndata yang removed paling belakang: \n{paling_belakang}')
