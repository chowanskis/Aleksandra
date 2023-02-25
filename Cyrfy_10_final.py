# Zadzanie 13 z informatyki strona 103
# Aleksandra Chowańska Klasa 8 A
# 
# Powtórz 10 razy algorytm rozbierania cyfry na liczby 
# Algorytm nie pozwala podać liczby ujemnej

# Definiujemy zmienną w której będziemy mieć ilośc powtórzeń
powtorzenia = range(10)

# Wiemy ile będzie powtórzeń więc używamy pętli for in
for i in powtorzenia:
    
    liczba = int(input("Podaj liczbę: "))

    # Jeżeli użytkownik poda liczbę mniejszą od zera
    # zapytaj go ponownie o liczę, zmien komunikat aby to zauważył.
    while liczba < 0:
        liczba = int(input("Podaj liczbę większą od zera: "))

    print("Cyfry liczby", liczba, "od ostatniej:")

    if liczba == 0:
        print(liczba)
    else: 
        while liczba != 0:
            cyfra = liczba % 10
            print(cyfra)
            liczba = (liczba - cyfra) // 10

input("\n\nAby zakończyć, naciśnij Enter.")