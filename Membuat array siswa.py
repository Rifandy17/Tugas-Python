# Membuat array siswa
siswa = []

# Membuat perulangan for
for i in range(3):
    
    # Mengecek nilai indeks
    print("")
    print("ini adalah indeks ke-",i)

    # Menerima inputan nama
    nama_siswa = input("Masukkan nama_saya : ")
    
    # Memasukkan hasil inputan nama ke array siswa
    siswa.append(nama_siswa)

print("")

# Membuat perulangan untuk mencetak data dari array siswa
for k in siswa :
    print("Nama Siswa : ", k)