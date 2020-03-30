import os

kitapListe=list()

menu="""
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitap Listesi
[Q] Çıkış

"""


def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı...")
    print("Ana menüye dönmek için 'enter'a basınız!")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap silme işlemi tamamlandı...")
        print("Ana menüye dönmek için 'enter'a basınız!")
        input()
    else:
        print("Aradığınız kitap bulunamadı!")
        print("Ana menüye dönmek için 'enter'a basınız!")
        input()

def listele(liste:list):
    for i in liste:
        print(liste.index(i)+1 , ")  Kitabın Adı : {}     -     Yazarı : {}  ".format(i[0],i[1]))

    print("Ana menüye dönmek için 'enter'a basınız!")
    input()

while True:
    os.system("cls") #Terminal ekranını temizler.
    print(menu)
    secim=input("İşleminizi seçiniz : ")

    if secim == "1":
        kitapIsim=input("Kitabın Adı : ")
        yazarIsim=input("Yazarın Adı : ")
        kitap=(kitapIsim,yazarIsim)
        kitapEkle(kitap,kitapListe)

    elif secim == "2":
        kitapIsim=input("Kitabın Adı : ")
        yazarIsim=input("Yazarın Adı : ")
        kitap=(kitapIsim,yazarIsim)
        kitapCikar(kitap,kitapListe)

    elif secim == "3":
        listele(kitapListe)

    elif secim == "q" or secim == "Q":
        print("Programdan çıkılıyor...")
        quit()

    else:
        print("Hatalı giriş yaptınız!")