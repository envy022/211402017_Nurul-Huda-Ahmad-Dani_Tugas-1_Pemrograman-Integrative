import math

# Input gaji selama satu tahun
gaji = float(input("Masukkan Gaji Anda: Rp  "))

# Mengghitung gaji perbulan 
gaji_bulanan = math.ceil(gaji / 12)

# Output perhitungan gaji perbulan 
print("Gaji Bulanan Anda adalah : Rp", gaji_bulanan)

