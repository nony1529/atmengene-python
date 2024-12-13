#Project 2
#ATM Engene
#Nony Zeina

#Membuat Variabel
pin = "282828"
saldo = 500000

#Pemeriksaan PIN
def verifikasi_pin():
    pin_pengguna = input("Silahkan Masukan PIN Anda = ")
    if pin_pengguna == pin:
        return True
    else :
        print("PIN Anda Salah, Silahkan Coba Lagi")
        return False

#Tampilan Awal/Menu
def menu():
    print("=" * 45)
    print("\t\tMENU ATM")
    print("=" * 45)
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

print("Selamat Datang Di ATM")

#Memanggil Verifikasi PIN Yang Telah Kita Buat
if verifikasi_pin():
    while True:
        menu()

#Input Pilihan Pada Menu
        pilih_menu = input("Silahkan Pilih Menu (1-4) : ")

        #Jika Memilih Menu 1
        if pilih_menu == "1":
            print("Saldo Anda Adalah: Rp", saldo)

        #Jika Memilih Menu 2
        elif pilih_menu == "2":
            tarik_tunai = int(input("Silahkan Masukan Nominal Nya : "))
            if tarik_tunai <= saldo:
                saldo -= tarik_tunai
                print("Penarikan Berhasil, Sisa Saldo Anda Sebesar : Rp", saldo)
            else:
               print("Maaf, Saldo Anda Tidak Mencukupi")

        #Jika Memilih Menu 3
        elif pilih_menu == "3":
            setor_tunai = int(input("Silahkan Masukan Nominal Nya : "))
            saldo += setor_tunai
            print("Setor Tunai Berhasil, Saldo Anda Sebesar : Rp", saldo)

        #Jika Memilih Menu 4
        elif pilih_menu == "4":
            print("Terima Kasih")
            break
        #Jika Pengguna Salah Input Menu
        else:
            print("Maaf, Pilihan Tidak Valid, Silahkan Pilih Menu (1-4)")