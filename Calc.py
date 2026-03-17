while True:
    print("\nWitaj w kalkulatorze, wybierz dzialanie z podanych poniżej:")
    print("1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie")

    wybrane_dzialanie = input()
    if wybrane_dzialanie not in {"1", "2", "3", "4"}:
        print("Nie ma takiego dzialania!")
        continue

    print("Wybrales dzialanie:", wybrane_dzialanie)

    liczba_a = float(input("Podaj liczbę a: "))
    liczba_b = float(input("Podaj liczbę b: "))

    if wybrane_dzialanie == "1":
        print("Wynik dodawania:", liczba_a + liczba_b)
    elif wybrane_dzialanie == "2":
        print("Wynik odejmowania:", liczba_a - liczba_b)
    elif wybrane_dzialanie == "3":
        print("Wynik mnożenia:", liczba_a * liczba_b)
    elif wybrane_dzialanie == "4":
        if liczba_b == 0:
            print("Nie można dzielić przez zero!")
        else:
            print("Wynik dzielenia:", liczba_a / liczba_b)

    kolejne = input("Czy chcesz wykonać kolejne działanie? (tak/nie): ")
    if kolejne == "nie":
        break

