# Membuat Program Biodata

# Membuat variabel nama_saya yang menerima inputan
nama_lengkap = input("Masukkan Nama Lengkap: ")

# Membuat variabel asal_daerah yang menerima inputan
asal_daerah = input("Masukkan Asal Daerah: ")

# Membuat array biodata untuk mengumpulkan hasil inputan
print("Melakukan pengumpulan hasil inputan kemudian disimpan di variabel biodata")
biodata = [ nama_lengkap, asal_daerah ]

index = 0
for isi_biodata in biodata :
    print(biodata[index])
    index = index + 1    