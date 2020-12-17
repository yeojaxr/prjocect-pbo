class Produk:
    def __init__(self, namaProduk, jumlah, harga):
        self.namaProduk = namaProduk
        self.jumlah = jumlah
        self.harga = harga
    
    def tampilkanPesanan(self):
        print(f"Nama Produk: {self.namaProduk} \nJumlah: {self.jumlah} \nHarga: {self.harga}")