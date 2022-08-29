# price = 10
# rating = 4.9
# name = "Paweł"
# is_published = False
# print(price)
#
# full_name = "Jacek Jakiś"
# age = 20
# is_new = True
#
# name = input('Jak masz na imię? ')
# print('Siemka ' + name)
# favorite_color = input('Jaki jest Twój ulubiony kolor? ')
# print('Paweł lubi ' + favorite_color)

# birth_year = input('Rok urodzenia: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# a = 5 #int
# b = 4.3 #float
# imie = "Paweł" #string
# czyDuzy = True #boolean (prawda lub fałsz)

# + dodwanie
# - odejmowanie
# * mnozenie
# / dzielenie
#
# () jak w matematyce kieruja kolejnoscia dzialania
#
# ** potegowanie
# // dzielenie w dol
# % modulo (reszta z dzielenia (licznik ułamka tylko!))

# dzielenie_cale = 9 / 2
# print(dzielenie_cale)
#
# dzielenie_zaokraglone = 9 // 2
# print(dzielenie_zaokraglone)

# zmienne!

# przykladowa zmiana podatku vat - zmienne

# Vat = 23
# obliczonyVat = (1 + Vat / 100)
#
# cenaKursuJavaNetto = 10
# cenaKursuAjaxNetto = 20
#
# cenaKursuJavaBrutto = cenaKursuJavaNetto * obliczonyVat
# cenaKursuAjaxBrutto = cenaKursuAjaxNetto * (1 + Vat / 100)
#
# print(cenaKursuJavaBrutto)
# print(cenaKursuJavaNetto)
#
# print(cenaKursuAjaxBrutto)
# print(cenaKursuAjaxNetto)

# --- 8
# first_name = input('Jak sie nazywasz? ')
# # print('Hello', first_name)
#
# if first_name == 'Kacper':
#     print('Cześć Kacper!')
# else:
#     print('Nie wiem kto ty???')

# a,b,c = 1,

# Python - podstawy w 60 minut yt / kacper sieradzinski.

# print('Hello World')
# first_name = input('Jak masz na imie? ')
# print('Hello', first_name)
#
# if first_name == 'Kacper':
#     print('Cześć Kacper!')
#
# else:
#     print('Nie wiem kto ty ale gadaj kto!')
#
# age = input('Ile masz lat? ')
#
# if int(age) >= 18:
#     print('Jesteś dorosły!')
#
# else:
#     print('No jeszcze nie...')
#     wait_years = 18 - int(age)
#     print('zaczekaj jeszcze:', wait_years, 'lat(a).')

# point_x = 1
# point_y = 2
#
# # tupla - krotka niemutowalna
# point = 1, 2
# print(point[0])
# print(point[1])
#
# print(point)
#
# # listy
#
# cities = ['Gdynia', 'Gdańsk', 'Sopot']
# cities.append('Warszawa')
# cities.append('Kraków')
# cities.append('Suwałki')
# print(cities[0])
# cities.sort()
# cities[-1] = 'Zakopane'
# print(cities)
#

# słowniki

capitals = {
    'Poland': 'Warszawa',
    'France': 'Paris',
    'Germany': 'Berlin'
}

print(capitals['Poland'])