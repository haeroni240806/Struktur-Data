#Input nama (validasi sederhana)
while True:
    nama = input("Masukkan nama anda: ")
    
    if nama.strip() != "":
        break
    else:
        print("Silahkan coba lagi")

# Input angka positif
while True:
    try:
        angka = int(input("Masukkan angka: "))
        
        if angka < 0:
            print("Harus positif!")
        else:
            break
    except ValueError:
        print("Input harus berupa angka!")

# Menampilkan tabel perkalian 1 sampai 10
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")