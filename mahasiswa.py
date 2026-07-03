# mahasiswa.py

from utils import contain_checker, is_number

mahasiswa = []


def tambah_mahasiswa():
    """Menambahkan data mahasiswa."""

    nim = input("Masukkan NIM   : ")
    nama = input("Masukkan Nama  : ")
    prodi = input("Masukkan Prodi : ")

    if not is_number(nim):
        print("NIM harus berupa angka!")
        return

    daftar_nim = [mhs["nim"] for mhs in mahasiswa]

    if contain_checker(nim, daftar_nim):
        print("NIM sudah terdaftar!")
        return

    mahasiswa.append({
        "nim": nim,
        "nama": nama,
        "prodi": prodi
    })

    print("Data mahasiswa berhasil ditambahkan.")


def lihat_mahasiswa():
    """Menampilkan seluruh data mahasiswa."""

    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return

    print("\n===== DAFTAR MAHASISWA =====")

    for i, mhs in enumerate(mahasiswa, start=1):
        print(f"{i}.")
        print(f"   NIM   : {mhs['nim']}")
        print(f"   Nama  : {mhs['nama']}")
        print(f"   Prodi : {mhs['prodi']}")
        print()


def cari_mahasiswa():
    """Mencari mahasiswa berdasarkan NIM."""

    nim = input("Masukkan NIM yang dicari : ")

    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            print("\nData ditemukan")
            print(f"NIM   : {mhs['nim']}")
            print(f"Nama  : {mhs['nama']}")
            print(f"Prodi : {mhs['prodi']}")
            return

    print("Data mahasiswa tidak ditemukan.")


def hapus_mahasiswa():
    """Menghapus data mahasiswa berdasarkan NIM."""

    nim = input("Masukkan NIM yang akan dihapus : ")

    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            mahasiswa.remove(mhs)
            print("Data mahasiswa berhasil dihapus.")
            return

    print("Data mahasiswa tidak ditemukan.")

# Test fitur mahasiswa, will delete later if main.py already created:)
if __name__ == "__main__":
    while True:
        print("\n===== TEST MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            lihat_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")