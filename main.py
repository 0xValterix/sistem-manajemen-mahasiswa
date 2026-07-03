import login
import mahasiswa

#Dikopi dan dimodif dari Kode Ferdi :D

#Biar termasuk dua fungsi :P

#Fungsi utama
def main():
    while True:
        print("\n===== MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mahasiswa.tambah_mahasiswa()
        elif pilihan == "2":
            mahasiswa.lihat_mahasiswa()
        elif pilihan == "3":
            mahasiswa.cari_mahasiswa()
        elif pilihan == "4":
            mahasiswa.hapus_mahasiswa()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

#Fungsi cek user login
def initcheck():
    if(login.login()):
        main()
    else:
        print("GAGAL LOGIN!")

initcheck()