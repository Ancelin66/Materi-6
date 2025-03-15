def kalkulasi_ips():
    # Memasukkan jumlah mata kuliah
    total_mk = int(input("Masukkan jumlah mata kuliah: "))
    
    # Bobot nilai
    konversi_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    akumulasi_bobot = 0
    total_sks = total_mk * 3  # SKS tetap 3 untuk setiap mata kuliah
    
    # Loop untuk setiap mata kuliah
    for idx in range(1, total_mk + 1):
        while True:
            huruf = input(f"Masukkan nilai (A/B/C/D) untuk mata kuliah {idx}: ").upper()
            if huruf in konversi_nilai:
                akumulasi_bobot += konversi_nilai[huruf] * 3  # SKS tetap 3
                break
            else:
                print("Nilai tidak valid, masukkan A, B, C, atau D.")
    
    # Menghitung IPS
    ips_final = akumulasi_bobot / total_sks
    print(f"Indeks Prestasi Semester (IPS) Anda: {ips_final:.2f}")

# Menjalankan program
kalkulasi_ips()
