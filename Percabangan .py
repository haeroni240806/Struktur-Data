# Input nama
nama = input("Masukan nama anda: ")

# Validasi nama (tidak boleh kosong)
if nama.strip() != "":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")
    exit()

# Input umur
umur = int(input("Masukan umur anda: "))

# Percabangan kondisi umur
if umur >= 18:
    print("Anda cukup umur")
elif umur < 0:
    print("Anda belum lahir")
elif umur < 18:
    print("Anda belum cukup umur")
elif umur > 60:
    print("Banyakin ibadah, bentar lagi mati")

print("Program selesai")