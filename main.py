# # price = 10
# # rating = 4.9
# # name = "Paweł"
# # is_published = False
# # print(price)
# #
# # full_name = "Jacek Jakiś"
# # age = 20
# # is_new = True
# #
# # name = input('Jak masz na imię? ')
# # print('Siemka ' + name)
# # favorite_color = input('Jaki jest Twój ulubiony kolor? ')
# # print('Paweł lubi ' + favorite_color)
#
# # birth_year = input('Rok urodzenia: ')
# # print(type(birth_year))
# # age = 2022 - int(birth_year)
# # print(type(age))
# # print(age)
#
# # weight_lbs = input('Weight (lbs): ')
# # weight_kg = int(weight_lbs) * 0.45
# # print(weight_kg)
#
# # a = 5 #int
# # b = 4.3 #float
# # imie = "Paweł" #string
# # czyDuzy = True #boolean (prawda lub fałsz)
#
# # + dodwanie
# # - odejmowanie
# # * mnozenie
# # / dzielenie
# #
# # () jak w matematyce kieruja kolejnoscia dzialania
# #
# # ** potegowanie
# # // dzielenie w dol
# # % modulo (reszta z dzielenia (licznik ułamka tylko!))
#
# # dzielenie_cale = 9 / 2
# # print(dzielenie_cale)
# #
# # dzielenie_zaokraglone = 9 // 2
# # print(dzielenie_zaokraglone)
#
# # zmienne!
#
# # przykladowa zmiana podatku vat - zmienne
#
# # Vat = 23
# # obliczonyVat = (1 + Vat / 100)
# #
# # cenaKursuJavaNetto = 10
# # cenaKursuAjaxNetto = 20
# #
# # cenaKursuJavaBrutto = cenaKursuJavaNetto * obliczonyVat
# # cenaKursuAjaxBrutto = cenaKursuAjaxNetto * (1 + Vat / 100)
# #
# # print(cenaKursuJavaBrutto)
# # print(cenaKursuJavaNetto)
# #
# # print(cenaKursuAjaxBrutto)
# # print(cenaKursuAjaxNetto)
#
# # --- 8
# # first_name = input('Jak sie nazywasz? ')
# # # print('Hello', first_name)
# #
# # if first_name == 'Kacper':
# #     print('Cześć Kacper!')
# # else:
# #     print('Nie wiem kto ty???')
#
# # a,b,c = 1,
#
# # Python - podstawy w 60 minut yt / kacper sieradzinski.
#
# # print('Hello World')
# # first_name = input('Jak masz na imie? ')
# # print('Hello', first_name)
# #
# # if first_name == 'Kacper':
# #     print('Cześć Kacper!')
# #
# # else:
# #     print('Nie wiem kto ty ale gadaj kto!')
# #
# # age = input('Ile masz lat? ')
# #
# # if int(age) >= 18:
# #     print('Jesteś dorosły!')
# #
# # else:
# #     print('No jeszcze nie...')
# #     wait_years = 18 - int(age)
# #     print('zaczekaj jeszcze:', wait_years, 'lat(a).')
#
# # point_x = 1
# # point_y = 2
# #
# # # tupla - krotka niemutowalna
# # point = 1, 2
# # print(point[0])
# # print(point[1])
# #
# # print(point)
# #
# # # listy
# #
# # cities = ['Gdynia', 'Gdańsk', 'Sopot']
# # cities.append('Warszawa')
# # cities.append('Kraków')
# # cities.append('Suwałki')
# # print(cities[0])
# # cities.sort()
# # cities[-1] = 'Zakopane'
# # print(cities)
# #
#
# # słowniki
#
# from random import choice
#
#
# capitals = {
#     'Poland': 'Warszawa',
#     'France': 'Paris',
#     'Germany': 'Berlin'
# }
#
# selected_country = choice(list(capitals.keys()))
#
# capital = input(f'What is the capital of {selected_country}? ')
#
# if capitals[selected_country] == capital:
#     print('Bardzo dobrze!')
# else:
#     print('Wcale nie! Chodziło nam o', capitals[selected_country])
#
# Guess the number!
#
# import random
# def guess(x):
#     random_number = random.randint(1, x)
#     quess = 0
#     while guess != random_number:
#         guess = input(f'Guess a number between 1 and {x}: ')
#         print(guess)
#
# guess(10)
#
# a = 5
# print(a)
#

# CS50 https://www.youtube.com/watch?v=5Jppcxc1Qzc

# Importowanie bibliotek - czym są funkcje? (Udemy)

# imie = "arkadiusz"
#
# imie = imie.capitalize()
#
# print(imie)

# Udemy Pobieranie i formatowanie danych od użytkownika oraz rzutowanie

# print("Kalkulator dodający:")
#
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
#
# print("Wynik dodawania to: ", a + b)
#
# 16. Operatory porównania

# Instrukcja warunkowa If oraz WCIĘCIA | UWAGA! | Python inaczej odbiera wcięcia

# a = int(input())
# b = int(input())
#
# if (a > b):
#     print("a jest większe od b")
# elif (b > a):
#     print("b jest większe od a")
# else:
#     print("a jest równe b")

# 19. Wartości różne od 0

# 20. Operatory Logiczne

# wartosc = int(input("Sprawdze, czy liczba jest od 1 do 10"))
#
# if (wartosc > 1):
#     if (wartosc < 10):
#         print("wartosc jest od 1 do 10")
#     if (wartosc > 10):
#         print("zbyt duzo")

# Operatory logiczne:
#
# and - i, or i not
# True - prawda
# or - lub

# a = 5
# b = 2
# if (a == 5 || b == 3):
#     print("tak")

# Pętla While:

# liczba = 5
#
# while liczba >= 0:
#     print(liczba)
#     liczba -= 1

# --- Ćwiczenia Pętle: Suma kolejnych liczb:

# wynik = 0

# i = 0
# while i < 4:
#     x = int(input("Podaj liczbę: "))
#
#     wynik += x
#     i += 1
#
# print("Wynik dodawania: ", wynik)

# Pętla for:::

# for i in range(121):
#     if (i % 2 == 0):
#         print("Liczba", i, " jest parzysta")
#
# print("Wynik dodawania liczb to: ", wynik)

# --- break i continue:

# wynik = 0
#
# i = 0
#
# while i < 3:
#     x = int(input("Podaj dodatnia liczbe: "))
#     if (x > 0):
#         wynik += x
#
#     else:
#         print("Miała być liczba dodatnia!")
#         continue
#     print("Aktualny wynik dodawania to:", wynik)

# Zadanie:
#
# Napisz program, który doda 3 parzyste liczby dodatnie podane przez użytkownika.
#
# Jeśli liczba będzie niedodatnia lub nieparzysta to program ma zapytać się o liczbę jeszcze raz. Program ma pytać się o liczby parzyste dodatnie dopóki nie doda 3 liczb.
#
#
#
# Wynik możesz wypisywać w pętli lub na końcu pętli. Pamiętaj liczby mają być i parzyste i dodatnie w tym samym momencie!
#
# wynik = 0
# i = 0
# while i < 3:
#     x = int(input("Podaj parzystą, dodatnią liczbę:"))
#     if (x > 0 and x % 2 == 0):
#         wynik += x
#     else:
#         print("Miała być liczba dodatnia parzysta, zapytam się o liczbę ponownie")
#         continue
#     print("Aktualny wynik dodawania to:", wynik)
#     i += 1

# Ćwiczenia - zgadywanie liczby:

