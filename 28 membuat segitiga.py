#akan dibuat program menggunakan loop untuk membuat segitiga
##memakai for
#membuat segitiga atas
'''
a = int(input('masukkan tinggi segitiga atas: '))
for i in range(a):
    a -= 1
    print("*"*a)

#membuat segitiga bawah

a = int(input('masukkan tinggi segitiga bawah: '))
b = 1
for i in range(a):
    print("*"*b)
    b += 1

##memakai while
#segitiga bawah
a= 0
b = int(input('masukkan tinggi segitiga bawah: '))
while a<b:
    a += 1
    print ("+"*a)

#segitiga atas
a= 0
b = int(input('masukkan tinggi segitiga atas: '))
while a<b:
    print ("+"*b)
    b -= 1

#membuat segitiga ganjil
a= 0
b = int(input('masukkan tinggi segitiga ganjil: '))
while a<=b:
    if a%2:
        print ("+"*a)
    a += 1

#membuat segitiga sama kaki
a= 0
b = int(input('masukkan tinggi segitiga sama kaki: '))
spasi = int(b/2)
while a<=b:
    if a%2:
        print (" "*spasi+"+"*a)
        spasi -= 1
        a += 1 #nambah a ketika a ganjil
    else: 
        a += 1 #nambah a ketika genap
'''

##membuat belah ketupat
a = 0 
b = int(input('masukan panjang diagonal: '))
spasi = int(b/2)
while a <= b :
    if a%2:
        print(" "*spasi+ 'o'*a)
        spasi -= 1
        a += 1
    else:
        a += 1
print(f'nilai a ; {a}')
print(f'nilai b ; {b}')
print(f'nilai spasi ; {spasi}')
while a > b:
    if a%2: #ganjil
        a -= 1
    else: #genap
        print(" "*spasi+ 'o'*a)
        spasi +=1
        a -= 1
print("akhir program")


















