def VatCalculator(price):
    return price + (price * 7 / 100)

price = int(input("Price : "))
print(VatCalculator(price))