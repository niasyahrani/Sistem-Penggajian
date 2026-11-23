
class Karyawan:
    jumlah_karyawan = 0

    # Constructor
    def __init__(self, nama, jabatan, gaji_pokok):
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji_pokok = gaji_pokok

        Karyawan.jumlah_karyawan += 1

    # Property untuk membaca gaji pokok
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah gaji pokok
    @gaji_pokok.setter
    def gaji_pokok(self, nilai):
        if nilai < 0:
            raise ValueError("Gaji tidak boleh negatif!")

        self.__gaji_pokok = nilai

    # Method untuk menghitung total gaji
    def hitung_gaji(self, tunjangan, potongan):
        return self.gaji_pokok + tunjangan - potongan

    # Method untuk menampilkan slip gaji
    def tampilkan_slip(self, tunjangan, potongan):
        total = self.hitung_gaji(tunjangan, potongan)

        print("\n===== SLIP GAJI KARYAWAN =====")
        print("Nama       :", self.nama)
        print("Jabatan    :", self.jabatan)
        print("Gaji Pokok : Rp", format(self.gaji_pokok, ","))
        print("Tunjangan  : Rp", format(tunjangan, ","))
        print("Potongan   : Rp", format(potongan, ","))
        print("------------------------------")
        print("Total Gaji : Rp", format(total, ","))
        print("==============================")

    # Class method untuk menghitung jumlah karyawan
    @classmethod
    def jumlah_terdaftar(cls):
        return cls.jumlah_karyawan

    # Static method untuk memeriksa kelayakan gaji
    @staticmethod
    def cek_gaji(gaji):
        return gaji >= 1000000


class SistemPenggajian:

    # Constructor
    def __init__(self):
        self.daftar_karyawan = []

    # Method untuk menambahkan karyawan
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    # Method untuk menampilkan semua karyawan
    def tampilkan_semua(self):
        print("\n=== DAFTAR KARYAWAN ===")

        for karyawan in self.daftar_karyawan:
            print(
                f"{karyawan.nama} - "
                f"{karyawan.jabatan} - "
                f"Rp {karyawan.gaji_pokok:,}"
            )


# ==============================
# PROGRAM UTAMA
# ==============================

# Membuat object karyawan
karyawan1 = Karyawan("Adnan", "Manager", 5000000)
karyawan2 = Karyawan("Rini", "Staff", 3500000)

# Membuat object sistem penggajian
sistem = SistemPenggajian()

# Menambahkan karyawan ke dalam sistem
sistem.tambah_karyawan(karyawan1)
sistem.tambah_karyawan(karyawan2)

# Menampilkan daftar karyawan
sistem.tampilkan_semua()

# Menampilkan slip gaji setiap karyawan
karyawan1.tampilkan_slip(500000, 200000)
karyawan2.tampilkan_slip(300000, 100000)

# Mengubah gaji pokok menggunakan setter
karyawan2.gaji_pokok = 4000000

print("\nGaji pokok Rini setelah diubah:")
print("Rp", format(karyawan2.gaji_pokok, ","))

# Menggunakan class method
print("\nJumlah karyawan:",
      Karyawan.jumlah_terdaftar())

# Menggunakan static method
print("Apakah gaji Adnan layak?",
      Karyawan.cek_gaji(karyawan1.gaji_pokok))
