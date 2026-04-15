def wczytaj_zadania():
    try:
        with open("zadania.txt", "r", encoding="utf-8") as plik:
            zadania = [linia.strip() for linia in plik.readlines()]
        return zadania
    except FileNotFoundError:
        return []

def zapisz_zadania(zadania):
    with open("zadania.txt", "w", encoding="utf-8") as plik:
        for zadanie in zadania:
            plik.write(zadanie + "\n")

def pokaz_zadania(zadania):
    if not zadania:
        print("\nBrak zadań na liście.\n")
    else:
        print("\nTwoje zadania:")
        for i, zadanie in enumerate(zadania, start=1):
            print(f"{i}. {zadanie}")
        print()

def dodaj_zadanie(zadania):
    nowe = input("Podaj treść nowego zadania: ")
    zadania.append(nowe)
    zapisz_zadania(zadania)
    print("Zadanie zostało dodane.\n")

def usun_zadanie(zadania):
    pokaz_zadania(zadania)

    if not zadania:
        return

    try:
        numer = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= numer <= len(zadania):
            usuniete = zadania.pop(numer - 1)
            zapisz_zadania(zadania)
            print(f'Usunięto zadanie: "{usuniete}"\n')
        else:
            print("Nieprawidłowy numer.\n")
    except ValueError:
        print("Musisz podać liczbę.\n")

def menu():
    zadania = wczytaj_zadania()

    while True:
        print("=== DO ZROBIENIA ===")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(zadania)
        elif wybor == "2":
            dodaj_zadanie(zadania)
        elif wybor == "3":
            usun_zadanie(zadania)
        elif wybor == "4":
            print("Koniec programu.")
            break
        else:
            print("Nie ma takiej opcji.\n")

menu()