class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def __str__(self):
        return f'Nama: {self.nama}, Jabatan: {self.jabatan}'

class DaftarKaryawan:
    def __init__(self):
        self.karyawan_list = []

    def tambah_karyawan(self, nama, jabatan):
        karyawan_baru = Karyawan(nama, jabatan)
        self.karyawan_list.append(karyawan_baru)
        print(f'Karyawan {nama} berhasil ditambahkan.')

    def tampilkan_karyawan(self):
        if not self.karyawan_list:
            print("Tidak ada karyawan yang terdaftar.")
            return
        for idx, karyawan in enumerate(self.karyawan_list, start=1):
            print(f'{idx}. {karyawan}')

    def update_karyawan(self, index, nama_baru, jabatan_baru):
        if 0 <= index < len(self.karyawan_list):
            self.karyawan_list[index].nama = nama_baru
            self.karyawan_list[index].jabatan = Jabatan_baru
            print(f'Karyawan pada index {index} berhasil diperbarui.')
        else:
            print("Index tidak valid.")

    def hapus_karyawan(self, index):
        if 0 <= index < len(self.karyawan_list):
            karyawan_terhapus = self.karyawan_list.pop(index)
            print(f'Karyawan {karyawan_terhapus.nama} berhasil dihapus.')
        else:
            print("Index tidak valid.")


def main():
    daftar_karyawan = DaftarKaryawan()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Update Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama karyawan: ")
            jabatan = input("Masukkan jabatan karyawan: ")
            daftar_karyawan.tambah_karyawan(nama, jabatan)
        elif pilihan == '2':
            daftar_karyawan.tampilkan_karyawan()
        elif pilihan == '3':
            index = int(input("Masukkan index karyawan yang ingin diupdate: ")) - 1
            nama_baru = input("Masukkan nama baru: ")
            jabatan_baru = input("Masukkan jabatan baru: ")
            daftar_karyawan.update_karyawan(index, nama_baru, jabatan_baru)
        elif pilihan == '4':
            index = int(input("Masukkan index karyawan yang ingin dihapus: ")) - 1
            daftar_karyawan.hapus_karyawan(index)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()