# Meminta pengguna memasukkan bilangan bulat
bilangan = float(input("Masukkan sebuah bilangan bulat: "))

# Menghitung hasil pembagian
hasil = bilangan / 3

# Menentukan jumlah angka di belakang koma sesuai kondisi
if hasil.is_integer():  # Jika hasilnya bilangan bulat
    hasil_str = hasil  # Tampilkan dengan 1 angka di belakang koma
else:
    hasil_str = "{:.3f}".format(hasil)  # Tampilkan dengan 3 angka di belakang koma

# Menampilkan hasil
print("Hasil pembagian:", hasil_str)

