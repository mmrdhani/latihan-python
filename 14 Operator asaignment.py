#disini akan belajar tentang operasi assignment
# operator ini ada tambah +=, kuang -=, kali *=, bagi /=
#ada juga modulus %=, floor division //=, pangkat **=
print('\n\n', 7*'=', 'PENJUMLAHAN', 7*'=')
a = 5
print('nilai a:' ,a)
# nilai a = a+1 serupa dengan a += 1
a += 1
print('Nilai dari a += 1 adalah: ', a)

print('\n\n', 7*'=', 'PENGURANGAN', 7*'=')
a = 5
print('nilai a:' ,a)
# nilai a = a-2 serupa dengan a -= 2
a -= 2
print('Nilai dari a -= 2 adalah: ', a)

print('\n\n', 7*'=', 'PERKALIAN', 7*'=')
a = 5
print('nilai a:', a)
# nilai a = a*8 serupa dengan a *= 8
a *= 8
print('Nilai dari a *= 8 adalah: ', a)

print('\n\n', 7*'=', 'PEMBAGIAN', 7*'=')
a = 24
print('nilai a:', a)
# nilai a = a/8 serupa dengan a /= 6
a /= 6
print('Nilai dari a /= 6 adalah: ', a)
"""nilai pembagian akan selalu bertipe float"""

print('\n\n', 7*'=', 'MODULUS', 7*'=')
a = 24
print('nilai a:', a)
a %= 5
print('Nilai dari a %= 4 adalah: ', a)

print('\n\n', 7*'=', 'FLOOR DIVISION', 7*'=')
a = 24
print('nilai a:', a)
a //= 5
print('Nilai dari a //= 4 adalah: ', a)
"""FLOOR DIVISION artinya adalah bilangan bulat terbesar
yang kurang dari hasil baginya"""

print('\n\n', 7*'=', 'PERPANGKATAN', 7*'=')
a = 4
print('nilai a:', a)
a **= 5
print('Nilai dari a **= 5 atau 4 pangakat 5 adalah: ', a)

#BERLAKU JUGA PADA OPERASI BITEWISE
print('\n\n', 7*'=', 'OR (|)', 7*'=')
c = True
print('nilai c adalah: ', c)
c |= False
# artinya c |= Fales adalah a = c | False
print( 'nilai c |= False adalah:', c)

c = False
print('\nnilai c adalah: ', c)
c |= False
print( 'nilai c |= False adalah:', c)

print('\n\n', 7*'=', 'AND (&)', 7*'=')
c = True
print('nilai c adalah: ', c)
c &= False
print( 'nilai c &= False adalah:', c)

c = False
print('\nnilai c adalah: ', c)
c &= False
print( 'nilai c &= False adalah:', c)

c = True
print('\nnilai c adalah: ', c)
c &= True
print( 'nilai c &= True adalah:', c)

print('\n\n', 7*'=', 'XOR (^)', 7*'=')
c = True
print('nilai c adalah: ', c)
c ^= False
print( 'nilai c ^= False adalah:', c)

c = False
print('\nnilai c adalah: ', c)
c ^= False
print( 'nilai c ^= False adalah:', c)

#GESER-GESER
#digunakan  untuk menggeser nilai pada biner
d = 0b0100
print('nilai d: ', d, 'binary: ', format(d, '04b'))
d >>= 2
print('Nilai d: ', d, "binary: ", format(d, '04b'))
d <<= 1
print('Nilai d: ', d, "binary: ", format(d, '04b'))

