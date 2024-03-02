hasil = 0
while True:
        # Membaca angka yang diinputkan oleh pengguna 
    bilangan  = int(input("Silahkan input sebuah bilangan (masukkan -1 jika ingin berhenti): "))

        # check jika angka yang diinputkan adalah -1 maka program akan berhenti 
    if bilangan  == -1:
        break  
    else:
        hasil += bilangan  # menambahkan angka ke variabel total

    # output hasil dari semua angka yang telah dihitung
print("Jumlah semua bilangan yuang telah di inputkan :", hasil)

