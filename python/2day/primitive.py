# Data Types

# String - jest to typ danych tekstowych
print(str("Hello world"))

# Integer - jest to typ danych liczbowych liczb całych

print(int(2 + 2))

# Float - jest to typ danych zmienno przecinkowych

print(float(0.1 + 0.2))


# boolean - jest to typ danych

# true

# false

string = "Hello"
print(type(string))

# type() sprawdza dany typ naszego kody

print(int(8 / 3))
print(round(8 / 3))  # round zaokrągla nam daną liczbe zmienno przecinkowa do liczby ktorej jest blizej
print(round(8 / 3, 2)) # Liczba po przecinka okresla ilosc liczb po przecinku ktore maja sie znajdowac w zaokrageleniu


print(8 // 3) # // jest znakiem pierwiastkwoania liczba 3 pokazuje jakiego stopnia ma byc to pierwiastek


score = 1

print(f"your score is {score}") # f string pozwala nam na dodawanie w naszym stringu zmiennych przez koniecznosci
                                # konieczenia stringa

week = 4
month = 12
print(week * month)
year = 90 * 48
print(year)

age = int(input("Podaj ilosc lat "))
year1 = age * 48
print(year1)

result = year - year1
print(result)