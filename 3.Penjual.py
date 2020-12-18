import sqlite3 
dbproject = "dbproject.sqlite"

class login():
    def __init__(self, username, kataSandi):
        self.username = username 
        self.kataSandi = kataSandi
    
    def profile(self):
        print(f"Username: {self.username} \nKata Sandi: {self.kataSandi} ")

        
class menambahkanProduk():
    def __init__(self, namaProduk, jumlah, harga):
        self.namaProduk = namaProduk
        self.jumlah = jumlah
        self.harga = harga

#membuat database 
    def createDatabase(self):
            conn = sqlite3.connect(dbproject)
            cursor = conn.cursor()
            query = "CREATE TABLE IF NOT EXISTS Produk(namaProduk TEXT NOT NULL, jumlah INTEGER NOT NULL, harga INTEGER NOT NULL)"
            cursor.execute(query)
            conn.commit()
            conn.close()

#menambahkan data pada tabel
    def addData(self):
        conn = sqlite3.connect(dbproject)
        cursor = conn.cursor()
        query = "INSERT INTO Produk VALUES(?,?,?)"

        isian = (self.namaProduk, self.jumlah, self.harga)
        cursor.execute(query, isian)
        conn.commit()
        conn.close()

#mengambil data
    def getData(self):
        conn = sqlite3.connect(dbproject)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Produk")

        hasil = cursor.fetchall()

        conn.close()

        for baris in hasil:
            for kolom in baris:
                print(kolom)
            print("===============================================")


    def deleteByNama(self, namaProduk):
        conn = sqlite3.connect(dbproject)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produk WHERE namaProduk = ?", (namaProduk,))
        conn.commit()
        conn.close()
        print("data berhasil dihapus")

produk = Menu("Srogun", 4, 60000)
produk1 = Menu("Nipple J-Lack", 3, 9900)

# menambahkan kedua objek ke dalam database
produk.addData()
produk1.addData()

produk1.getData()
print("===============================================")
produk1.deleteByNama("Pur")
produk1.getData() 