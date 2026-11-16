from smartphone import Smartphone

smartphone = Smartphone("Apple", "iPhone 17", "+79201088899")
smartphone1 = Smartphone("Samsung", "Galaxy A56", "+79281087799")
smartphone2 = Smartphone("Xiaomi", "POCO X7 Pro", "+79081085688")
smartphone3 = Smartphone("Realme ", "GT 7 Pro ", "+79011585681")
smartphone4 = Smartphone("Honor ", " 200 Pro  ", "+7911585381")

catalog = [smartphone, smartphone1, smartphone2, smartphone3, smartphone4]

for smartphone in catalog:
    print(smartphone)
