import login
import mahasiswa

#Dikopi dari Kode Ferdi :P
#Dimodif
#Main func

if(login.login()):
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
else:
    print("GAGAL LOGIN!")