##WIDTH AND MULTILINE

data_nama = "Ucup"
data_tinggi = 170.5
data_berat = 70
data_umur = 19
data_nomor_sepatu = 43

data_string = f"nama= {data_nama}, tinggi: {data_tinggi}, berat= {data_berat}, umur: {data_umur}, nomor sepatu: {data_nomor_sepatu}"
print(data_string)

print(8*"="+ "STRING DENGAN NEWLINE"+ "="*8)
#bisa ditambah dengan enter, newlinr, \n
data_string = f"nama= {data_nama}, \ntinggi: {data_tinggi}, \nberat= {data_berat}, \numur: {data_umur}, \nnomor sepatu: {data_nomor_sepatu}"
print(data_string)

print(8*"="+ "STRING DENGAN NEWLINE"+ "="*8)
print(f"""
nama= {data_nama}
tinggi= {data_tinggi}
berat= {data_berat}
umur= {data_umur}
nomor sepatu = {data_nomor_sepatu}
""")

print(8*"="+ "MENGATUR LEBAR"+ "="*8)
data_str = f"""
nama         = {data_nama:>8}
tinggi       = {data_tinggi:>8}
berat        = {data_berat:>8}
umur         = {data_umur:>8}
nomor sepatu = {data_nomor_sepatu:>8}
"""
print(data_str)