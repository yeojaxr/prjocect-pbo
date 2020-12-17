from Produk import Produk
class Pembayaran(Produk):
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

pesanan  = Produk("Trimezyn", 1, 7500)
pesanan1 = Pembayaran("Nipple J-Lock", 3, 9900, "Bank BNI", "COD")

print('==============================')
pesanan1.checkout("pur")
pesanan1.checkout("antraks", "biodin")
pesanan1.checkout("cardiovit", "obat cacing", "sapi")

print('''==============================
Nama Produk = {}
Jumlah = {}
Harga = {}
Total Pembayaran = {}
Metode Pembayaran = {}
Opsi Pengiriman = {}
=============================='''.format(pesanan1.namaProduk, pesanan1.jumlah, pesanan1.harga, pesanan1.totalBayar(), pesanan1.metodePembayaran, pesanan1.opsiPengiriman))
