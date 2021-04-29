class Siswa :

    def __init__(self, nis, nama, kelas) :
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #decorator
    @property
    def nis(self) :
        pass

    #getter
    @nis.getter
    def nis(self) :
        return self.__nis

    #setter 
    @nis.setter
    def nis (self, newnis) :
        self.__nis = newnis

wawan = Siswa(16354, "Sopan Setiawan", "XI MIPA 1")

print(wawan.nis)
wawan.nis = 123456
print(wawan.nis)