# Aleksanda Chowańska klasa 8A
# Zadanie zaliczeniowe z trójkątów na informatykę. 
# Zadanie wykonano w VisualStudio Code , środowisko Fedora 
#
#

# Podaj liczbę wierszy trójkąta.
# Pamiętaj input da ci Stringa, więc go rzutujemy na int
wiersz = int(input("Wpisz liczbę wierszy (1-10): "))

# Jeżeli wiersz jest większy niż 10 to zamieniamy go na 10
# Taka była dopuszczalna liczba maksymalna.
if wiersz > 10:
    wiersz = 10

# Jeżeli jest mniejszy od 1 (0 lub liczba ujemna)
# To liczba wierszy zamieniana jest na wartoś 1 minimalną
if wiersz < 1:
    wiersz = 1

# Zmienna, pojemnik na ilość gwiazdek do obliczenia
ileGwiazdek = 0

# Pętla zewnętrzna rysuje wiersze (1 do 11 = czyli 10 wierszy)
# Dla 10 wierszy pętla wygląda tak:  Wiersze (1 2 3 4 5 6 7 8 9 10) 11 porzuci
for i in range(1, wiersz+1):
    
    # 1 Pętla wewnętrzna - liczy ilość pustych kratek 
    for pusteMiejsce in range(1, (wiersz-i)+1):
        print(end=" ")
   
    # Wylicza ile ma być gwiazdek i je drukuje jeden rząd gwiazdek
    # Dla 10 rzędów (2*10) - 1 = 19 gwiazdek
    while ileGwiazdek!=(2*i-1):
        print("*", end="")
        ileGwiazdek += 1
   
    ileGwiazdek = 0
    print()
    