class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membuat objek persegi panjang dengan panjang = 3 dan lebar = 2
    pp = PersegiPanjang(3, 2)

    # Menampilkan string representation dari objek
    print(pp)

    # Menampilkan hasil perhitungan keliling dan luas
    print("Keliling:", pp.hitung_keliling(), "cm")
    print("Luas    :", pp.hitung_luas(), "cm²")

   


