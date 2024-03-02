# Angka yang diinputkan oleh pengguna
bilangan = int(input("Silahkan Masukkan Bilangan : "))

# menghitung angka yang yang dinputkan pengguna
total = sum(range(1, bilangan + 1))

# Formatkan output sesuai dengan permintaan
print("Jumlah Semua Bilangan dari 1 sampai", bilangan, "adalah:", end=" ")

# Outputkan deret bilangan dari 1 sampai bilangan yang dimasukkan pengguna
for i in range(1, bilangan + 1):
    if i == bilangan:
        print(i, end=" ")
    else:
        print(i, end=" + ")

# Outputkan hasil total
print("=", total)
