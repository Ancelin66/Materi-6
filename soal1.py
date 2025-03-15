def perkalian(x, y):
    # jika salah satu bilangan adalah 0, hasilnya pasti 0
    if x == 0 or y == 0:
        return 0
    
    # jika kedua bilangan negatif, ubah menjadi positif agar lebih mudah dihitung
    elif x < 0 and y < 0:
        return perkalian(-x, -y)
    
    # jika hanya x yang negatif, ubah menjadi positif dan beri tanda negatif di hasilnya
    elif x < 0:
        return -perkalian(-x, y)
    
    # jika hanya y yang negatif, ubah menjadi positif dan beri tanda negatif di hasilnya
    elif y < 0:
        return -perkalian(x, -y)
    
    # melakukan perkalian dengan menggunakan penjumlahan sebanyak x kali
    return sum(y for _ in range(x))

# contoh penggunaan
bil1 = 6
bil2 = 5
# menampilkan perhitungan yang sesuai dengan contoh
print(f"{bil1} x {bil2} = {' + '.join([str(bil2)] * bil1)} = {perkalian(bil1, bil2)}")

bil3 = 7
bil4 = 10
print(f"{bil3} x {bil4} = {' + '.join([str(bil4)] * bil3)} = {perkalian(bil3, bil4)}")


