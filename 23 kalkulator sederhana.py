"""
Akan dibuat kalkulator sederhana yang memanfaatkan 
percabangan if, else, dan elif dengan operasi +, -, x, /
"""

print('KALKULATOR'.center(38,"="))
angka1 = float(input("masukkan bilangan: "))
operator = input('masukkan operator (+,-,x,/)')
angka2 = float(input("masukkan bilangan: "))

if operator == "x":
    hasil= angka1*angka2
    print(f'hasil perkalian {angka1} x {angka2} = {hasil}')
elif operator == "/":
    hasil= angka1/angka2
    print(f'hasil pembagian {angka1} / {angka2} = {hasil}')
elif operator == "+":
    hasil= angka1/angka2
    print(f'hasil penjumlahan {angka1} + {angka2} = {hasil}')
elif operator == "-":
    hasil= angka1-angka2
    print(f'hasil pengurangan {angka1} - {angka2} = {hasil}')
else:
    print(f'operator: {operator} yang anada masukkan salah!')

