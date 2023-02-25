# Zadzanie 13 z informatyki strona 103
# Aleksandra Chowańska Klasa 8 A
# 
# Powtórz 10 razy algorytm rozbierania cyfry na liczby 
#
# UWAGA: Algorytm nie działa dla liczb ujemnych.

# Definiujemy zmienną w której będziemy mieć ilośc powtórzeń
powtorzenia = range(10)

# Wiemy ile będzie powtórzeń więc używamy pętli for in
for i in powtorzenia:
    
    liczba = int(input("podaj liczbę: "))

    print("Cyfry liczby", liczba, "od ostatniej:")

    if liczba == 0:
        print(liczba)
    else: 
        while liczba != 0:
            cyfra = liczba % 10
            print(cyfra)

            # Silne dzielenie np: 159 // 10 = 15
            # Słabe dzielenie np: 159 /  10 = 15.9
            liczba = (liczba) // 10

input("\n\nAby zakończyć, naciśnij Enter.")