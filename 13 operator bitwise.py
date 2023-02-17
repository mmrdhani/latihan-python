#ini adalah operator tambahan karena mungkin ada yang butuh
#operator bitwise adalah operator  biner 
#jadi operasi pada masing-masing bite
#operasi bitwise ada 4, yaitu or (|), and (&), not (~), dan xor (^)
a = 5
b = 3
print('====OPERASI OR (|)====\n')
print('nilai a: ', a, "binary: ", format(a, '08b'))
print('nilai b: ', b, "binary: ", format(b, "08b"))
#arti dari format(a, '08b') adalah menunjukkann format:
# 0 jika nilai kosong, terdapat 8 digit, dan "b" untuk kode binernya
c = a|b
print('------------------------------ (|)')
print('nilai', a, '|', b, ' = ', c, "binary:", format(c, "08b"))
#jadi nilai or (|) dioperasikan kepada digit masing-masing biner pada indeks yang sama

print('\n\n====OPERASI AND (&)====\n')
print('nilai a: ', a, "binary: ", format(a, '08b'))
print('nilai b: ', b, "binary: ", format(b, "08b"))
c = a&b
print('------------------------------ (&)')
print('nilai', a, '&', b, ' = ', c, "binary:", format(c, "08b"))
#jadi nilai and (&) dioperasikan kepada digit masing-masing biner pada indeks yang sama

print('\n\n====OPERASI XOR (^)====\n')
print('nilai a: ', a, "binary: ", format(a, '08b'))
print('nilai b: ', b, "binary: ", format(b, "08b"))
c = a^b
print('------------------------------ (^)')
print('nilai', a, '^', b, ' = ', c, "binary:", format(c, "08b"))
#jadi nilai xor (^) dioperasikan kepada digit masing-masing biner pada indeks yang sama

print('\n\n====OPERASI NOT (~)====\n')
print('nilai a: ', a, "binary: ", format(a, '08b'))
c = ~a
print('------------------------------ (~)')
print('nilai  not a (~a) = ', c, 'binary:', format(c, "08b"))

d = 0b00000101
e = 0b11111111
c = d^e
print('nilai d        ', format(d, '08b'))
print('nilai e        ', format(e, '08b'))
print('------------------------------ (^)')
print('nilai ~a:', c, 'binary:', format(c, '08b'))
 