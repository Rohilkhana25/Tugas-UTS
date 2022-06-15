import datetime

class pemilu:
    def  coblos():
        print('''Daftar nama paslon
        1. rohil dan yusuf
        2. akbar dan adi 
        ''')
        nomer = input('masukan nomer paslon = ')
        if nomer == "1":
            print('rohil dan akbar')

        elif nomer == "2":
            print('akbar dan adi')

        else :
            print('nomer tidak sesuai')
x = pemilu
x.coblos()
x = datetime.datetime.now()
print(x)

        