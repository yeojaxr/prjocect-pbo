class Registrasi:
    def __init__(self, namaDepan,namaBelakang, email,noHp,sandi):
        self.namaDepan = namaDepan
        self.namaBelakang = namaBelakang
        self.email = email
        self.noHp = noHp
        self.sandi = sandi 

    def dataDiri(self):
        print(f"Nama Depan: {self.namadepan}. Nama Belakang: {self.namaBelakang}. Email: {self.email}. No Hp: {self.noHp}. Kata Sandi : {self.sandi}" )

