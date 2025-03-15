def deret_ganjil(start, end):
    # jika start lebih besar dari end, urutan mundur, jika tidak urutan maju
    if start > end:
        return [i for i in range(start, end - 1, -1) if i % 2 != 0]
    else:
        return [i for i in range(start, end + 1) if i % 2 != 0]

#input dari pengguna
nilai_awal = int(input("Masukkan nilai awal: "))
nilai_akhir = int(input("Masukkan nilai akhir: "))

#memanggil fungsi dan mencetak hasil
deret = deret_ganjil(nilai_awal, nilai_akhir)
print("Deret bilangan ganjil:", ", ".join(map(str, deret)))
