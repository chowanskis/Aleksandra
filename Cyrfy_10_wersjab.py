# Zadzanie 13 z informatyki strona 103
# Aleksandra Chowańska Klasa 8 A
# 
# Powtórz 10 razy algorytm rozbierania cyfry na liczby 
#
# UWAGA: Algorytm nie działa dla liczb ujemnych.

# Definiujemy zmienną w której będziemy mieć ilośc powtórzeń
powtorzenia = 10

# Wiemy ile będzie powtórzeń więc powinniśmy użyć pętli for in
# ale my użyjemy pętli while
while powtorzenia != 0:
    
    powtorzenia = (powtorzenia - 1)

    liczba = int(input("podaj liczbę: "))

    print("Cyfry liczby", liczba, "od ostatniej:")

    if liczba == 0:
        print(liczba)
    else: 
        while liczba != 0:
            cyfra = liczba % 10
            print(cyfra)
            liczba = (liczba - cyfra) // 10

input("\n\nAby zakończyć, naciśnij Enter.")