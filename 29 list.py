#list data angka
list_data = [1,2,3]
print(f'list angka: {list_data}')
print(f"tipe data {type(list_data)}\n")
#tipe daata dari list adalah <class 'list'>

#list data string
list_str = ['aku', 'kamu', 'kita', 'kami']
print(f'list string: {list_str}\n')

#list data boolean
list_bool = [True, False, False, True]
print(f'list boolean: {list_bool}\n')

#list campuran
list_campuran =[1,2,'kamu', 3, 'aku', True, 'otong', False]
print(f'list campuran: {list_campuran}\n')

##cara menuliskan lsit dengan lebih advance
# dengan range
rentang = list(range(0,10)) 
#karena list itu tipe data, perlu dicasting dulu dati tipe range ke tipe list
#dibaca range dari 0 sampai sebelum 10
print(f'list range dari 0 sampai sebelum 10: \n{rentang}\n')

#dengan for
list_pake_for = [i for i in range(0,15)]
print(f'list pake for: \n{list_pake_for}')

#dengan for dan if
list_pake_for_if = [i for i in range(0,15) if i%2==1 ]
#disyaratkan i mod 2 = 1, artinya yang dibagi 2 bersisa satu akan diprint
print(f'list pake for if: \n{list_pake_for_if}')

list_pake_for_if = [i for i in range(0,15) if i%2==0 ]
#disyaratkan i mod 2 = 0, artinya yang habis dibagi 2 akan diprint
print(f'list pake for if: \n{list_pake_for_if}')

