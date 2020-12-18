class menu():
    def __init__(self, namaProduk, jumlah, harga):
        self.namaProduk = namaProduk
        self.jumlah = jumlah
        self.harga = harga

class menuBeli(menu):
    def __init__(self, totalHarga, totalBayar):
        super().__init__(namaProduk,jumlah,harga)
        self.totalHarga = totalHarga
        self.totalBayar = totalBayar

class Pembayaran(menu):
    def __init__(self, namaProduk, jumlah, harga, metodePembayaran, opsiPengiriman):
        super().__init__(namaProduk, jumlah, harga)
        self.metodePembayaran = metodePembayaran
        self.opsiPengiriman = opsiPengiriman

    def totalBayar(self):
        total = self.jumlah * self.harga
        return total

    #overriding
    def tampilkanPesanan(self):
        print(f"Nama Produk: {self.namaProduk} \nJumlah: {self.jumlah} \nHarga: {self.harga} \nTotal Bayar: {totalBayar()} \nMetode Pembayaran: {self.metodePembayaran} \nOpsi Pengiriman: {self.opsiPengiriman}")

    #overloading
    def checkout(self, *produk):
        if len(produk) == 1:
            print(f"Produk yang dipesan yaitu {produk[0]}")
        elif len(produk) == 2:
            print(f"Produk yang dipesan yaitu {produk[0]} dan {produk[1]}")
        else:
            print(f"Produk yang dipesan yaitu {produk[0]}, {produk[1]}, dan {produk[2]}")

class login():
    def __init__(self, username, kataSandi):
        self.username = username 
        self.kataSandi = kataSandi
    
    def profile(self):
        print(f"Username: {self.username} \nKata Sandi: {self.kataSandi} ")